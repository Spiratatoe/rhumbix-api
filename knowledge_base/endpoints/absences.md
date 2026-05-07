# Absences

- **Function:** `get_absences` (in `src/absences/api.py`)
- **HTTP path:** `/absences/` (full URL = `${RHUMBIX_BASE_URL}/absences/`)
- **Returns:** `List[Dict]` — paginated, all pages collected.

## Import

```python
from src.absences.api import get_absences
```

## Parameters

All optional. `None` values are stripped before sending. Booleans are sent as-is when not `None` (passing `False` is a meaningful filter).

| Name | Type | Notes |
|---|---|---|
| page_size | int | Results per page. |
| start_date | str | YYYY-MM-DD. |
| end_date | str | YYYY-MM-DD. |
| is_approved | bool | Filter for approved status. |
| status | str | e.g. `PENDING`, `APPROVED`. Overrides `is_approved` if both are given. |
| employee | str | Employee's `company_supplied_id`. |
| last_updated | str | Datetime in `YYYY-MM-DDThh:mm:ss.ffffffZ` format. |
| include_deleted | bool | If true, retrieve deleted records. |
| group_id | List[int] | One or more group IDs. |
| include_subgroups | bool | If true and `group_id` is supplied, include subgroups. |

## Example call

```python
rows = get_absences(start_date="2024-02-01", end_date="2024-02-29")
```

## Output shape

Top-level keys (from `output/absences_date_params.json`):
- `code`
- `deleted_on`
- `employee`
- `end_time`
- `id`
- `is_approved`
- `shift_date`
- `start_time`
- `status`
- `timezone`
- `type`
- `work_shift_key`
- `last_updated`

## Failure modes

- Network / non-2xx -> `get_all_paginated_results` logs and returns `[]`.
- Empty list is ambiguous (no records vs. error) — check logs.
- 401/403 -> bad `RHUMBIX_API_KEY`. 400 -> unknown filter or malformed date.
