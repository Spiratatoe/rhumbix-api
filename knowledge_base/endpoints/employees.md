# Employees

- **Function:** `get_employees` (in `src/employees/api.py`)
- **HTTP path:** `/employees/` (full URL = `${RHUMBIX_BASE_URL}/employees/`)
- **Returns:** `List[Dict]` — paginated, all pages collected.

## Import

```python
from src.employees.api import get_employees
```

## Parameters

All optional. `None` values are stripped. Booleans are sent when not `None`.

| Name | Type | Notes |
|---|---|---|
| page_size | int | Results per page. |
| last_updated | str | Datetime, `YYYY-MM-DDThh:mm:ss.ffffffZ`. |
| is_active | bool | Filter by active status. |
| company_supplied_id | List[str] | One or more company-supplied IDs. |
| group_id | List[int] | One or more group IDs. |
| include_subgroups | bool | If true and `group_id` supplied, include subgroups. |
| email_address | str | Filter by email address. |
| phone_number | str | Filter by phone number. |
| include_deleted | bool | If true, retrieve deleted records. |

## Example call

```python
rows = get_employees(is_active=True, last_updated="2025-12-01T00:00:00.000000Z")
```

## Output shape

Top-level keys (from `output/employees_all_params.json`):
- `certifications`
- `cico_pin`
- `cico_qr_code`
- `classification`
- `cohort_permissions`
- `cohorts`
- `company_supplied_id`
- `custom_fields`
- `disabled_status`
- `email`
- `enable_login`
- `first_name`
- `is_active`
- `last_name`
- `licenses`
- `phone`
- `text_alerts_ok`
- `trade`
- `unions`
- `user_role`
- `veteran_status`
- `created_on`
- `last_active`

## Failure modes

- Network / non-2xx -> `get_all_paginated_results` logs and returns `[]`.
- Empty list is ambiguous (no records vs. error) — check logs.
- 401/403 -> bad `RHUMBIX_API_KEY`. 400 -> unknown filter or malformed date.
