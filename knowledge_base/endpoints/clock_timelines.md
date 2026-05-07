# Clock In / Clock Out Timelines

- **Function:** `get_clock_in_clock_out_timelines` (in `src/clock_timelines/api.py`)
- **HTTP path:** `/clock_in_clock_out_timelines/` (full URL = `${RHUMBIX_BASE_URL}/clock_in_clock_out_timelines/`)
- **Returns:** `List[Dict]` — paginated, all pages collected.

## Import

```python
from src.clock_timelines.api import get_clock_in_clock_out_timelines
```

## Parameters

All optional. `None` values are stripped before sending.

| Name | Type | Notes |
|---|---|---|
| page_size | int | Results per page. |
| foreman | List[str] | One or more foreman `company_supplied_id`s. |
| start_date | str | YYYY-MM-DD. |
| end_date | str | YYYY-MM-DD (inclusive). |
| job_number | List[str] | One or more job numbers. |
| worker | List[str] | One or more worker `company_supplied_id`s. |

## Example call

```python
rows = get_clock_in_clock_out_timelines(start_date="2025-12-15", end_date="2025-12-15")
```

## Output shape

Top-level keys (per docstring example):
- `id`
- `working_minutes`
- `break_minutes`
- `meal_minutes`
- `job_numbers`
- `worker`
- `foreman`
- `shift_date`
- `start_time`
- `end_time`
- `entry_ids`

## Failure modes

- Network / non-2xx -> `get_all_paginated_results` logs and returns `[]`.
- Empty list is ambiguous (no records vs. error) — check logs.
- 401/403 -> bad `RHUMBIX_API_KEY`. 400 -> unknown filter or malformed date.
