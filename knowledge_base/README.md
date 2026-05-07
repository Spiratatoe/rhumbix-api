# Rhumbix API — Knowledge Base

Token-efficient reference for using this codebase to call the Rhumbix REST API.

- **Read this file first** for setup, conventions, and the endpoint index.
- **Open `endpoints/<resource>.md`** only for the specific endpoint(s) you need (params, output shape, failure behavior).

---

## 1. Environment

Create `.env` at the repo root:

```
RHUMBIX_API_KEY="<your_api_key>"
RHUMBIX_BASE_URL="https://api.rhumbix.com/v1"
```

Loaded by `src/config.py` via `python-dotenv`. Both vars are required; `main.py` aborts at startup if either is missing.

Install:

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
source .venv/bin/activate       # Unix
pip install -r requirements.txt
```

---

## 3. Calling pattern (uniform across all resources)

Every `src/<resource>/api.py` follows this template — `employees` shown as the canonical example. To add a new endpoint, copy this and swap the constant, function name, and kwargs.

```python
EMPLOYEES_ENDPOINT = "/employees/"


def get_employees(
    page_size: Optional[int] = None,
    last_updated: Optional[str] = None,
    is_active: Optional[bool] = None,
    company_supplied_id: Optional[List[str]] = None,
    group_id: Optional[List[int]] = None,
    include_subgroups: Optional[bool] = None,
    email_address: Optional[str] = None,
    phone_number: Optional[str] = None,
    include_deleted: Optional[bool] = None,
) -> List[Dict]:
    """
    Retrieves a list of employees from the Rhumbix API.

    Args:
        page_size (Optional[int]): Number of results to return per page.
        last_updated (Optional[str]): Retrieve data updated after this datetime.
        is_active (Optional[bool]): Filter by active status.
        company_supplied_id (Optional[List[str]]): Filter by one or more company-supplied IDs.
        group_id (Optional[List[int]]): Filter by one or more group IDs.
        include_subgroups (Optional[bool]): If true and group_id is supplied, include subgroups.
        email_address (Optional[str]): Filter by email address.
        phone_number (Optional[str]): Filter by phone number.
        include_deleted (Optional[bool]): If true, retrieve deleted records.

    Returns:
        List[Dict]: A list of employee dictionaries.
    """
    url = f"{BASE_URL}{EMPLOYEES_ENDPOINT}"
    headers = {'x-api-key': API_KEY, 'Content-Type': 'application/json'}
    params = {
        "page_size": page_size,
        "last_updated": last_updated,
        "is_active": is_active,
        "company_supplied_id": company_supplied_id,
        "group_id": group_id,
        "include_subgroups": include_subgroups,
        "email_address": email_address,
        "phone_number": phone_number,
        "include_deleted": include_deleted,
    }

    # Remove None values from params
    params = {k: v for k, v in params.items() if v is not None}

    results = get_all_paginated_results(url, headers, params=params)

    return results
```

Invariants every module obeys:

1. `<RESOURCE>_ENDPOINT` constant holds the path appended to `BASE_URL`.
2. Headers are always `{"x-api-key": API_KEY, "Content-Type": "application/json"}`.
3. Every filter is a kwarg defaulting to `None`; `None` values are stripped before the request.
4. The function returns `get_all_paginated_results(url, headers, params=params)` — a flat `List[Dict]` across all pages.

### Pagination contract (`src/utils.py`)

The Rhumbix API returns `{"results": [...], "next": "<full_url_or_null>"}`. The helper:

- Walks `next` until null, accumulating `results`.
- Drops `params` after the first request — they're embedded in `next`.
- Returns `List[Dict]` of every record across all pages.

### Error behavior

`get_all_paginated_results` catches `requests.exceptions.RequestException`, logs the status code + body, and **returns `[]`**.

> **Important:** an empty list means *either* "no matching records" *or* "request failed". Check logs (level `INFO`) to distinguish. Functions never raise to the caller.



## 4. Endpoint index

| Resource | Function | Path | Detail file |
|---|---|---|---|
| absences | `get_absences` | `/absences/` | [absences.md](endpoints/absences.md) |
| absences_history | `get_absences_history` | `/absences/history/` | [absences_history.md](endpoints/absences_history.md) |
| absence_types | `get_absence_types` | `/absence_types/` | [absence_types.md](endpoints/absence_types.md) |
| budgets | `get_budgets` | `/budgets/` | [budgets.md](endpoints/budgets.md) |
| change_orders | `get_change_orders` | `/change_orders/` | [change_orders.md](endpoints/change_orders.md) |
| clock_entries | `get_clock_entries` | `/clock_entries/` | [clock_entries.md](endpoints/clock_entries.md) |
| clock_timelines | `get_clock_in_clock_out_timelines` | `/clock_in_clock_out_timelines/` | [clock_timelines.md](endpoints/clock_timelines.md) |
| cohorts | `get_cohorts` | `/cohorts/` | [cohorts.md](endpoints/cohorts.md) |
| companies | `get_companies` | `/companies/` | [companies.md](endpoints/companies.md) |
| company_classifications | `get_company_classifications` | `/company_classifications/` | [company_classifications.md](endpoints/company_classifications.md) |
| company_groups | `get_rhumbix_ou_list`, `get_company_groups_details` | `/company_groups/` | [company_groups.md](endpoints/company_groups.md) |
| company_trades | `get_company_trades` | `/company_trades/` | [company_trades.md](endpoints/company_trades.md) |
| cost_codes | `get_cost_codes` | `/cost_codes/` | [cost_codes.md](endpoints/cost_codes.md) |
| cost_code_controls | `get_cost_code_controls` | `/cost_code_controls/` | [cost_code_controls.md](endpoints/cost_code_controls.md) |
| cost_items | `get_cost_items` | `/cost_items/` | [cost_items.md](endpoints/cost_items.md) |
| deleted_timekeeping_entries | `get_deleted_timekeeping_entries` | `/deleted_timekeeping_entries/` | [deleted_timekeeping_entries.md](endpoints/deleted_timekeeping_entries.md) |
| email_alerts | `get_email_alerts` | `/email_alerts/` | [email_alerts.md](endpoints/email_alerts.md) |
| employees | `get_employees` | `/employees/` | [employees.md](endpoints/employees.md) |
| employees_groups | `get_employees_groups` | `/employees_groups/` | [employees_groups.md](endpoints/employees_groups.md) |
| employees_pricing | `get_employees_pricing` | `/employees_pricing/` | [employees_pricing.md](endpoints/employees_pricing.md) |
| employees_projects | `get_employees_projects` | `/employees_projects/` | [employees_projects.md](endpoints/employees_projects.md) |
| employee_shifts_and_breaks | `get_employee_shifts_and_breaks` | `/employee_shifts_and_breaks/` | [employee_shifts_and_breaks.md](endpoints/employee_shifts_and_breaks.md) |
| employee_shifts_and_breaks_history | `get_employee_shifts_and_breaks_history` | `/employee_shifts_and_breaks/history/` | [employee_shifts_and_breaks_history.md](endpoints/employee_shifts_and_breaks_history.md) |
| employee_shift_details | `get_employee_shift_details` | `/employee_shift_details/` | [employee_shift_details.md](endpoints/employee_shift_details.md) |
| equipment | `get_equipment` | `/equipment/` | [equipment.md](endpoints/equipment.md) |
| equipment_pricing | `get_equipment_pricing` | `/equipment_pricing/` | [equipment_pricing.md](endpoints/equipment_pricing.md) |
| field_folders | `get_field_folders` | `/field_folders/` | [field_folders.md](endpoints/field_folders.md) |
| field_folder_notes | `get_field_folder_notes` | `/field_folder_notes/` | [field_folder_notes.md](endpoints/field_folder_notes.md) |
| groups | `get_groups` | `/groups/` | [groups.md](endpoints/groups.md) |
| locked_time_periods | `get_locked_time_periods` | `/locked_time_periods/` | [locked_time_periods.md](endpoints/locked_time_periods.md) |
| materials | `get_materials` | `/materials/` | [materials.md](endpoints/materials.md) |
| material_pricing | `get_material_pricing` | `/material_pricing/` | [material_pricing.md](endpoints/material_pricing.md) |
| notes | `get_notes` | `/notes/` | [notes.md](endpoints/notes.md) |
| picklists | `get_picklists` | `/picklists/` | [picklists.md](endpoints/picklists.md) |
| picklist_items | `get_picklist_items` | `/picklist_items/` | [picklist_items.md](endpoints/picklist_items.md) |
| projects | `get_projects` | `/projects/` | [projects.md](endpoints/projects.md) |
| project_equipment | `get_project_equipment` | `/project_equipment/` | [project_equipment.md](endpoints/project_equipment.md) |
| project_materials | `get_project_materials` | `/project_materials/` | [project_materials.md](endpoints/project_materials.md) |
| quantity_entries | `get_quantity_entries` | `/quantity_entries/` | [quantity_entries.md](endpoints/quantity_entries.md) |
| shift_extra_entries | `get_shift_extra_entries` | `/shift_extra_entries/` | [shift_extra_entries.md](endpoints/shift_extra_entries.md) |
| shift_extra_entries_history | `get_shift_extra_entries_history` | `/shift_extra_entries/history/` | [shift_extra_entries_history.md](endpoints/shift_extra_entries_history.md) |
| shift_extra_schemas | `get_shift_extra_schemas` | `/shift_extra_schemas/` | [shift_extra_schemas.md](endpoints/shift_extra_schemas.md) |
| start_stop_types | `get_start_stop_types` | `/start_stop_types/` | [start_stop_types.md](endpoints/start_stop_types.md) |
| timekeeping_entries | `get_timekeeping_entries` | `/timekeeping_entries/` | [timekeeping_entries.md](endpoints/timekeeping_entries.md) |
| timekeeping_entries_history | `get_timekeeping_entries_history` | `/timekeeping_entries/history/` | [timekeeping_entries_history.md](endpoints/timekeeping_entries_history.md) |
| timekeeping_statuses | `get_timekeeping_statuses` | `/timekeeping_statuses/` | [timekeeping_statuses.md](endpoints/timekeeping_statuses.md) |
| timeoff_requests | `get_timeoff_requests` | `/timeoff_requests/` | [timeoff_requests.md](endpoints/timeoff_requests.md) |
| users | `get_users` | `/users/` | [users.md](endpoints/users.md) |
| workflow_entries | `get_workflow_entries` | `/workflow_entries/` | [workflow_entries.md](endpoints/workflow_entries.md) |
| workflow_entries_history | `get_workflow_entries_history` | `/workflow_entries/history/` | [workflow_entries_history.md](endpoints/workflow_entries_history.md) |
| work_shift_details | `get_work_shift_details` | `/work_shift_details/` | [work_shift_details.md](endpoints/work_shift_details.md) |

> Paths in the table are read from each module's `*_ENDPOINT` constant. If a row is missing, the module wasn't present at index time — check `src/` directly.

---

## 5. Conventions for failure handling

When wrapping these functions in a higher-level skill:

- Treat `[] ` as ambiguous (no data **or** error). If you need to disambiguate, instrument `get_all_paginated_results` to raise instead of swallow.
- HTTP non-2xx responses are logged but suppressed. Common causes: bad `RHUMBIX_API_KEY` → 401/403; unknown filter param → 400; bad date format (must be ISO 8601, often with trailing `Z`) → 400.
- The helper uses no retry / no backoff. Long syncs against a flaky network may return partial results silently — add a wrapper if that matters.
- `params` containing `None` are dropped, but empty strings (`""`) and `False` are sent. Don't pass `False` unless you mean it.
