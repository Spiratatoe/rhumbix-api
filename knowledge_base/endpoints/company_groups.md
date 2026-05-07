# Company Groups (Organizational Units)

This module exports **two** functions:

- `get_rhumbix_ou_list` — convenience wrapper returning only `id` + `name`, sorted by name.
- `get_company_groups_details` — full company-group records.

Both call `/company_groups/` (full URL = `${RHUMBIX_BASE_URL}/company_groups/`).

## Import

```python
from src.company_groups.api import get_rhumbix_ou_list, get_company_groups_details
```

---

## `get_rhumbix_ou_list`

- **Returns:** `List[Dict]` with two keys per row: `id`, `name`. Empty list on error or if response lacks expected columns.
- Internally calls `get_company_groups_details()` (no filters), then filters columns via pandas.

### Parameters

None.

### Example call

```python
ous = get_rhumbix_ou_list()
```

### Output shape

- `id`
- `name`

---

## `get_company_groups_details`

- **Returns:** `List[Dict]` — paginated, all pages collected.

### Parameters

All optional. Note: only sets the param if truthy (so `page_size=0` is also skipped).

| Name | Type | Notes |
|---|---|---|
| last_updated | str | Datetime, `YYYY-MM-DDThh:mm:ss.ffffffZ`. |
| page_size | int | Results per page. |

### Example call

```python
rows = get_company_groups_details(last_updated="2025-12-16T16:45:02.323544Z")
```

### Output shape

Top-level keys (per docstring example):
- `id`
- `name`
- `description`
- `parent_id`
- `children_ids`
- `employees`
- `grants_employee_access`
- `grants_project_access`
- `cohorts`
- `cico_settings`

## Failure modes

- Network / non-2xx -> `get_all_paginated_results` logs and returns `[]`.
- `get_rhumbix_ou_list` additionally returns `[]` if the response lacks both `id` and `name` columns (logs an error).
- 401/403 -> bad `RHUMBIX_API_KEY`. 400 -> unknown filter or malformed date.
