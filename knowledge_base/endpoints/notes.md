# Notes

- **Function:** `get_notes` (in `src/notes/api.py`)
- **HTTP path:** `/notes/` (full URL = `${RHUMBIX_BASE_URL}/notes/`)
- **Returns:** `List[Dict]` — paginated, all pages collected.

## Import

```python
from src.notes.api import get_notes
```

## Parameters

All optional. `None` values are stripped before sending.

| Name | Type | Notes |
|---|---|---|
| page_size | int | Results per page. |
| job_number | str | Filter by job number. |
| start_date | str | YYYY-MM-DD. |
| end_date | str | YYYY-MM-DD. |
| last_updated | str | Datetime, `YYYY-MM-DDThh:mm:ss.ffffffZ`. |

## Example call

```python
rows = get_notes(job_number="190375", start_date="2024-02-01", end_date="2024-02-29")
```

## Output shape

No captured sample. Run once and inspect; common Rhumbix fields include `id`, `created_on`, `last_updated`.

## Failure modes

- Network / non-2xx -> `get_all_paginated_results` logs and returns `[]`.
- Empty list is ambiguous (no records vs. error) — check logs.
- 401/403 -> bad `RHUMBIX_API_KEY`. 400 -> unknown filter or malformed date.
