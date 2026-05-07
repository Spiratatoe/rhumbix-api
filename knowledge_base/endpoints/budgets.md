# Budgets

- **Function:** `get_budgets` (in `src/budgets/api.py`)
- **HTTP path:** `/budgets/` (full URL = `${RHUMBIX_BASE_URL}/budgets/`)
- **Returns:** `List[Dict]` — paginated, all pages collected.

## Import

```python
from src.budgets.api import get_budgets
```

## Parameters

All optional. `None` values are stripped before sending.

| Name | Type | Notes |
|---|---|---|
| page_size | int | Results per page. |
| job_number | str | Filter by a specific job number. |
| source | str | Budget source. Valid: `ERP`, `FIELD`. |
| last_updated | str | Datetime in `YYYY-MM-DDThh:mm:ss.ffffffZ` format. |
| cost_code | str | Filter by the `code` field of the budget's cost code. |

## Example call

```python
rows = get_budgets(job_number="7269636", source="FIELD")
```

## Output shape

Top-level keys (per docstring example):
- `job_number`
- `cost_code`
- `quantities`
- `hours`
- `source`

## Failure modes

- Network / non-2xx -> `get_all_paginated_results` logs and returns `[]`.
- Empty list is ambiguous (no records vs. error) — check logs.
- 401/403 -> bad `RHUMBIX_API_KEY`. 400 -> unknown filter or malformed date.
