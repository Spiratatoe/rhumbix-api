# Field Folder Notes

- **Function:** `get_field_folder_notes` (in `src/field_folder_notes/api.py`)
- **HTTP path:** `/field_folder_notes/` (full URL = `${RHUMBIX_BASE_URL}/field_folder_notes/`)
- **Returns:** `List[Dict]` — paginated, all pages collected.

## Import

```python
from src.field_folder_notes.api import get_field_folder_notes
```

## Parameters

All optional. `None` values are stripped. Booleans (e.g. `has_photos=False`) are sent when not `None` — meaningful filters.

| Name | Type | Notes |
|---|---|---|
| page_size | int | Results per page. |
| project | List[int] | One or more project IDs. |
| author | List[int] | One or more author IDs. |
| shift_date_from | str | Date filter. |
| shift_date_to | str | Date filter. |
| created_on_from | str | Datetime filter. |
| created_on_to | str | Datetime filter. |
| last_updated_from | str | Datetime filter. |
| last_updated_to | str | Datetime filter. |
| is_private | bool | Filter by private flag. |
| is_daily_report | bool | Filter for daily reports. |
| has_photos | bool | Filter notes with/without photos. |
| has_files | bool | Filter notes with/without files. |
| has_weather | bool | Filter notes with/without weather. |
| has_delays | bool | Filter notes with/without delays. |
| has_visitors | bool | Filter notes with/without visitors. |
| has_tags | bool | Filter notes with/without tags. |
| tags | List[str] | Filter by tags. |
| cost_codes | List[str] | Filter by cost codes. |
| equipment | List[int] | Filter by equipment IDs. |
| employees | List[str] | Filter by employees. |
| note_type | List[str] | Filter by note type. |
| include_deleted | bool | If true, retrieve deleted records. |

## Example call

```python
rows = get_field_folder_notes(project=[12345], has_photos=True)
```

## Output shape

No captured sample. Run once and inspect; common Rhumbix fields include `id`, `created_on`, `last_updated`.

## Failure modes

- Network / non-2xx -> `get_all_paginated_results` logs and returns `[]`.
- Empty list is ambiguous (no records vs. error) — check logs.
- 401/403 -> bad `RHUMBIX_API_KEY`. 400 -> unknown filter or malformed date.
