# Company Classifications

- **Function:** `get_company_classifications` (in `src/company_classifications/api.py`)
- **HTTP path:** `/company_classifications/` (full URL = `${RHUMBIX_BASE_URL}/company_classifications/`)
- **Returns:** `List[Dict]` — paginated, all pages collected.

## Import

```python
from src.company_classifications.api import get_company_classifications
```

## Parameters

All optional. `None` values are stripped before sending.

| Name | Type | Notes |
|---|---|---|
| page_size | int | Results per page. |

## Example call

```python
rows = get_company_classifications()
```

## Output shape

No captured sample. Run once and inspect; common Rhumbix fields include `id`, `created_on`, `last_updated`.

## Failure modes

- Network / non-2xx -> `get_all_paginated_results` logs and returns `[]`.
- Empty list is ambiguous (no records vs. error) — check logs.
- 401/403 -> bad `RHUMBIX_API_KEY`. 400 -> unknown filter or malformed date.
