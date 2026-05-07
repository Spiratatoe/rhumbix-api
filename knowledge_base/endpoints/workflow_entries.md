# Workflow Entries

- **Function:** `get_workflow_entries` (in `src/workflow_entries/api.py`)
- **HTTP path:** `/workflow_entries/` (full URL = `${RHUMBIX_BASE_URL}/workflow_entries/`)
- **Returns:** `List[Dict]` — paginated, all pages collected.

## Import

```python
from src.workflow_entries.api import get_workflow_entries
```

## Parameters

All optional. `None` values are stripped. Booleans are sent when not `None`.

| Name | Type | Notes |
|---|---|---|
| page_size | int | Results per page. |
| job_number | str | Filter by job number. |
| created_start_date | str | YYYY-MM-DD. |
| created_end_date | str | YYYY-MM-DD. |
| schema_id | int | Filter by schema ID. |
| schema_name | str | Filter by schema name. |
| variants | str | Filter by variants. |
| last_updated | str | Datetime, `YYYY-MM-DDThh:mm:ss.ffffffZ`. |
| status | str | Filter by status. |
| include_deleted | bool | If true, retrieve deleted records. |
| is_active | bool | Filter by active status. |
| expiration | int | Filter by expiration. |

## Example call

```python
rows = get_workflow_entries(schema_name="Daily Report", created_start_date="2024-02-01", created_end_date="2024-02-29")
```

## Output shape

No captured sample. Run once and inspect; common Rhumbix fields include `id`, `created_on`, `last_updated`.

## Failure modes

- Network / non-2xx -> `get_all_paginated_results` logs and returns `[]`.
- Empty list is ambiguous (no records vs. error) — check logs.
- 401/403 -> bad `RHUMBIX_API_KEY`. 400 -> unknown filter or malformed date.
