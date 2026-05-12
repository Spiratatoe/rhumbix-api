"""
Take real samples from output/samples/ and write anonymized versions to
knowledge_base/endpoints/samples/.

Goals
-----
- Preserve every key, type, list length, and overall shape.
- Replace PII (names, emails, phones, addresses) with fake-but-plausible values.
- Replace identifiers (employee IDs, job numbers, UUIDs, cost codes, etc.)
  with fake equivalents. Same real value -> same fake value across all files.
- Keep dates, statuses, booleans, and numeric metrics untouched (not PII).
- Drop rows whose role looks like "test" or "admin" if there are enough
  non-admin rows after dropping. Otherwise keep them but anonymize.

The mapping is deterministic (hash-based) so re-runs produce stable output.
"""
import hashlib
import json
import os
import re
import uuid as _uuid
from typing import Any, Dict, List

SRC_DIR = os.path.join("output", "samples")
DST_DIR = os.path.join("knowledge_base", "endpoints", "samples")

# --- deterministic helpers -------------------------------------------------

SEED = "rhumbix-fake-v1"


def _h(*parts: Any) -> int:
    """Stable 64-bit-ish int hash of the inputs."""
    raw = SEED + "|" + "|".join(str(p) for p in parts)
    return int(hashlib.sha1(raw.encode()).hexdigest()[:12], 16)


FIRST_NAMES = [
    "Alex", "Sam", "Jordan", "Casey", "Riley", "Morgan", "Taylor", "Quinn",
    "Avery", "Reese", "Drew", "Cameron", "Jamie", "Skyler", "Hayden", "Sage",
    "Parker", "Rowan", "Emery", "Finley", "Harper", "Kai", "Logan", "Marlowe",
    "Oakley", "Phoenix", "River", "Sawyer", "Tate", "Wren",
]
LAST_NAMES = [
    "Carter", "Hayes", "Brooks", "Reed", "Bailey", "Walsh", "Knox", "Pratt",
    "Mason", "Lane", "Cole", "Sloan", "Fox", "Quinn", "Vance", "Pope",
    "Wells", "Ortiz", "Rivera", "Bell", "Diaz", "Mendez", "Soto", "Vega",
    "Lara", "Cano", "Cruz", "Marin", "Solis", "Aguilar",
]
STREETS = [
    "Maple Ave", "Oak St", "Pine Rd", "Cedar Way", "Birch Blvd", "Elm Ct",
    "Willow Dr", "Aspen Ln", "Sycamore Pl", "Spruce Pkwy",
]
CITIES = ["Springfield", "Riverton", "Lakeside", "Hillcrest", "Fairview"]
PROJECT_NOUNS = [
    "Civic Center", "Logistics Hub", "Distribution Site", "Office Tower",
    "Training Facility", "Operations Yard", "Storage Depot", "Warehouse Bay",
    "Sub-Station", "Mixed-Use Block",
]
PROJECT_ADJECTIVES = [
    "North", "South", "East", "West", "Riverside", "Greenfield", "Downtown",
    "Uptown", "Lakeview", "Hillside",
]
COHORT_LABELS = [
    "Bravo Crew", "Echo Team", "Delta Squad", "Foxtrot Group", "Golf Unit",
    "Hotel Crew", "Charlie Team", "Alpha Group", "India Squad", "Juliet Unit",
]
COMPANY_NAMES = [
    "Acme Build Co", "Apex Contractors", "Beacon Industrial",
    "Cornerstone Group", "Delta Trade Partners", "Evergreen Builders",
    "Foundry Works", "Granite Industrial", "Horizon Contracting",
    "Ironclad Construction",
]


def fake_first(seed: Any) -> str:
    return FIRST_NAMES[_h("first", seed) % len(FIRST_NAMES)]


def fake_last(seed: Any) -> str:
    return LAST_NAMES[_h("last", seed) % len(LAST_NAMES)]


def fake_email(seed: Any) -> str:
    f = fake_first(seed).lower()
    l = fake_last(seed).lower()
    return f"{f}.{l}@example.com"


def fake_phone(seed: Any) -> str:
    n = _h("phone", seed)
    area = 200 + n % 700
    mid = 100 + (n // 1000) % 900
    end = 1000 + (n // 1000000) % 9000
    return f"+1{area}{mid}{end}"


def fake_address(seed: Any) -> str:
    n = _h("addr", seed)
    num = 100 + n % 9900
    street = STREETS[n % len(STREETS)]
    city = CITIES[(n // 7) % len(CITIES)]
    return f"{num} {street}, {city}, TX 78700, USA"


def fake_project_name(seed: Any) -> str:
    n = _h("proj", seed)
    return f"{PROJECT_ADJECTIVES[n % len(PROJECT_ADJECTIVES)]} {PROJECT_NOUNS[(n // 7) % len(PROJECT_NOUNS)]}"


def fake_cohort_name(seed: Any) -> str:
    return COHORT_LABELS[_h("cohort", seed) % len(COHORT_LABELS)]


def fake_company_name(seed: Any) -> str:
    return COMPANY_NAMES[_h("co", seed) % len(COMPANY_NAMES)]


def fake_uuid(seed: Any) -> str:
    h = hashlib.sha1((SEED + "|uuid|" + str(seed)).encode()).hexdigest()
    return str(_uuid.UUID(h[:32]))


def fake_numeric_id(seed: Any, length: int) -> str:
    """Return a digit-only string of the same length as the input."""
    if length <= 0:
        length = 6
    h = hashlib.sha256((SEED + "|nid|" + str(seed)).encode()).hexdigest()
    # convert hex to decimal digits string and slice/pad
    n = int(h, 16)
    s = str(n)
    if len(s) < length:
        s = s.rjust(length, "0")
    return s[:length]


def fake_alnum_id(seed: Any, length: int) -> str:
    alphabet = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"
    n = _h("alnum", seed)
    out = []
    for _ in range(length):
        out.append(alphabet[n % len(alphabet)])
        n //= len(alphabet)
        if n == 0:
            n = _h("alnum2", seed, len(out))
    return "".join(out)


def fake_job_number(seed: Any) -> str:
    return fake_numeric_id(("job", seed), 6)


def fake_cico_pin(seed: Any) -> str:
    return fake_numeric_id(("cico", seed), 4)


def fake_cost_code(seed: Any) -> str:
    """Preserve dotted segments — replace digit segments with fake digits,
    keep trailing alpha suffix (e.g., '...657940L')."""
    s = str(seed)
    parts = s.split(".")
    out_parts = []
    for i, p in enumerate(parts):
        m = re.match(r"^(\d+)([A-Za-z]*)$", p)
        if m:
            digits, suffix = m.group(1), m.group(2)
            out_parts.append(fake_numeric_id((seed, i), len(digits)) + suffix)
        else:
            out_parts.append(p)
    return ".".join(out_parts)


# --- field-rule based replacement ------------------------------------------

# These employee-ID-shaped string keys map consistently via the registry.
EMPLOYEE_ID_FIELDS = {
    "employee", "foreman", "creator", "worker", "author", "user",
    "company_supplied_id", "approved_by", "submitted_by", "modifier",
    "modified_by", "created_by", "updated_by", "signed_by",
}
EMPLOYEE_LIST_FIELDS = {
    "employees", "employee_permissions", "workers", "foremen", "authors",
    "users", "approvers",
}
PROJECT_FIELDS = {"job_number"}
PROJECT_LIST_FIELDS = {"job_numbers"}

UUID_KEY_HINTS = ("uuid",)  # any key containing 'uuid'


def _is_uuid_like(s: str) -> bool:
    return isinstance(s, str) and re.fullmatch(r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}", s) is not None


def _looks_like_numeric_id(s: str) -> bool:
    return isinstance(s, str) and s.isdigit() and 3 <= len(s) <= 12


SIGNED_URL_PATTERNS = (
    "AWSAccessKeyId=",
    "x-amz-security-token",
    "X-Amz-Signature",
    "X-Amz-Credential",
    "Signature=",
)


def _scrub_value(key: str, value: Any) -> Any:
    if value is None:
        return None
    kl = key.lower() if isinstance(key, str) else ""

    # --- string values -----------------------------------------------------
    if isinstance(value, str):
        if value == "":
            return ""

        # scrub any URL carrying AWS signed-URL credentials, regardless of key
        if value.startswith(("http://", "https://")) and any(p in value for p in SIGNED_URL_PATTERNS):
            return f"https://example.com/files/{fake_alnum_id(value, 12).lower()}.jpg"

        # known URL keys: replace with a stable fake URL
        if kl in ("fullsize", "thumbnail", "photo", "photo_url", "image_url", "url", "signature_url", "avatar_url"):
            return f"https://example.com/files/{fake_alnum_id(value, 12).lower()}.jpg"

        # project_id-as-string -> stable fake job number
        if kl == "project_id" and value.isdigit():
            return fake_job_number(value)

        # explicit field-name rules
        if kl == "email" or kl.endswith("_email") or kl == "client_contact_email":
            return fake_email(value)
        if kl == "first_name":
            return fake_first(value)
        if kl == "last_name":
            return fake_last(value)
        if kl in ("name",):  # context-dependent; treat as label only in objects
            return value  # handled per-resource in outer pass
        if kl == "phone" or kl.endswith("_phone") or kl == "phone_number":
            return fake_phone(value)
        if kl == "address" or kl.endswith("_address") or kl == "client_contact_address":
            return fake_address(value)
        if kl == "client_name":
            return fake_company_name(value)
        if kl == "client_contact_name":
            return f"{fake_first(value)} {fake_last(value)}"
        if kl == "cico_pin":
            return fake_cico_pin(value) if value else ""
        if kl == "cico_qr_code":
            return fake_alnum_id(value, 8) if value else ""
        if kl == "cost_code":
            return fake_cost_code(value)
        if kl in PROJECT_FIELDS:
            return fake_job_number(value)
        if kl == "work_shift_key":
            return fake_alnum_id(value, len(value))
        if kl in EMPLOYEE_ID_FIELDS:
            if _looks_like_numeric_id(value):
                return fake_numeric_id(value, len(value))
            return fake_alnum_id(value, max(4, len(value)))
        if "uuid" in kl:
            return fake_uuid(value)

        # generic catch-alls based on value shape
        if _is_uuid_like(value):
            return fake_uuid(value)
        # emails embedded in unusual keys
        if "@" in value and re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+", value):
            return fake_email(value)

        return value

    # --- numeric values ----------------------------------------------------
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        # most numeric values are durations / counts / IDs; don't touch
        return value

    # everything else is handled recursively by the caller
    return value


def _scrub(key: str, value: Any) -> Any:
    """Recursive scrub. `key` is the parent key that contains this value."""
    if isinstance(value, dict):
        return {k: _scrub(k, v) for k, v in value.items()}
    if isinstance(value, list):
        kl = key.lower() if isinstance(key, str) else ""
        # List-of-employee-IDs treatment
        if kl in EMPLOYEE_LIST_FIELDS:
            out = []
            for item in value:
                if isinstance(item, str) and _looks_like_numeric_id(item):
                    out.append(fake_numeric_id(item, len(item)))
                elif isinstance(item, str):
                    out.append(fake_alnum_id(item, max(4, len(item))))
                else:
                    out.append(_scrub(key, item))
            return out
        if kl in PROJECT_LIST_FIELDS:
            return [fake_job_number(v) if isinstance(v, str) else _scrub(key, v) for v in value]
        return [_scrub(key, v) for v in value]
    return _scrub_value(key, value)


# Per-resource tweaks for fields whose meaning is resource-specific (e.g.,
# 'name' on a project is a project name, on a cohort is a cohort label).
RESOURCE_NAME_RULES = {
    "projects": fake_project_name,
    "cohorts": fake_cohort_name,
    "companies": fake_company_name,
    "company_groups": fake_company_name,
}


def post_process(resource: str, rows: List[Dict]) -> List[Dict]:
    rule = RESOURCE_NAME_RULES.get(resource)
    if rule and isinstance(rows, list):
        for r in rows:
            if isinstance(r, dict) and isinstance(r.get("name"), str) and r["name"]:
                r["name"] = rule(r["name"])
            if resource == "projects":
                # description sometimes contains the real project name
                if isinstance(r.get("description"), str) and r["description"]:
                    r["description"] = "Sample project description"
    return rows


def looks_like_admin(row: Dict) -> bool:
    if not isinstance(row, dict):
        return False
    role = (row.get("user_role") or "").upper()
    fn = (row.get("first_name") or "").lower()
    csid = (row.get("company_supplied_id") or "").upper()
    return role == "ADMIN" or fn in {"rhumbix", "admin", "test"} or csid in {"RMBX", "ADMIN", "TEST"}


def maybe_skip_admin(rows: List[Dict]) -> List[Dict]:
    """If we have plenty of non-admin rows, drop admin/test rows. Otherwise keep them."""
    if not isinstance(rows, list) or not rows:
        return rows
    non_admin = [r for r in rows if not looks_like_admin(r)]
    if len(non_admin) >= 3:
        return non_admin
    return rows


def main():
    if not os.path.isdir(SRC_DIR):
        raise SystemExit(f"No source dir: {SRC_DIR}")
    os.makedirs(DST_DIR, exist_ok=True)

    files = sorted(f for f in os.listdir(SRC_DIR) if f.endswith(".json") and not f.startswith("_"))
    summary = {}
    for f in files:
        src = os.path.join(SRC_DIR, f)
        with open(src, encoding="utf-8") as fh:
            data = json.load(fh)
        resource = os.path.splitext(f)[0]
        if isinstance(data, list):
            data = maybe_skip_admin(data)
            data = [_scrub("__root__", row) for row in data]
            data = post_process(resource, data)
        else:
            data = _scrub("__root__", data)
        dst = os.path.join(DST_DIR, f)
        with open(dst, "w", encoding="utf-8") as fh:
            json.dump(data, fh, indent=2)
        n = len(data) if isinstance(data, list) else 1
        summary[resource] = n

    with open(os.path.join(DST_DIR, "_index.json"), "w", encoding="utf-8") as fh:
        json.dump(summary, fh, indent=2)
    print("Anonymized samples written:")
    for k, v in summary.items():
        print(f"  {k}: {v} rows")


if __name__ == "__main__":
    main()
