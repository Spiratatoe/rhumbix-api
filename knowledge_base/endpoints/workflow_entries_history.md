# Workflow Entries History

- **Function:** `get_workflow_entries_history` (in `src/workflow_entries_history/api.py`)
- **HTTP path:** `/workflow_entries/history/` (full URL = `${RHUMBIX_BASE_URL}/workflow_entries/history/`)
- **Returns:** `List[Dict]` — paginated, all pages collected.

## Import

```python
from src.workflow_entries_history.api import get_workflow_entries_history
```

## Parameters

All optional. `None` values are stripped before sending.

| Name | Type | Notes |
|---|---|---|
| page_size | int | Results per page. |
| ids | List[int] | Filter by one or more workflow entry IDs. |
| history_start_date | str | Retrieve history from this date onwards. |
| history_end_date | str | Retrieve history up to this date. |
| history_type | str | One of `CREATED`, `UPDATED`, `DELETED`. |

## Example call

```python
rows = get_workflow_entries_history(history_type="UPDATED", history_start_date="2024-01-01")
```

## Output shape

No captured sample. Top-level keys not documented — caller should inspect first response.

## Failure modes

- Network / non-2xx -> `get_all_paginated_results` logs and returns `[]`.
- Empty list is ambiguous (no records vs. error) — check logs.
- 401/403 -> bad `RHUMBIX_API_KEY`. 400 -> unknown filter or malformed date.
