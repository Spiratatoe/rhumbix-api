# Companies

- **Function:** `get_companies` (in `src/companies/api.py`)
- **HTTP path:** `/companies/` (full URL = `${RHUMBIX_BASE_URL}/companies/`)
- **Returns:** `List[Dict]` — paginated, all pages collected.

## Import

```python
from src.companies.api import get_companies
```

## Parameters

All optional. `None` values are stripped before sending.

| Name | Type | Notes |
|---|---|---|
| page_size | int | Results per page. |
| job_number | str | Filter by a specific job number. |

## Example call

```python
rows = get_companies(job_number="190375")
```

## Output shape

Top-level keys (per docstring example):
- `company_key`
- `name`

## Failure modes

- Network / non-2xx -> `get_all_paginated_results` logs and returns `[]`.
- Empty list is ambiguous (no records vs. error) — check logs.
- 401/403 -> bad `RHUMBIX_API_KEY`. 400 -> unknown filter or malformed date.
