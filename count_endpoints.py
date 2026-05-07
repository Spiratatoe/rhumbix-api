"""
Script to count records from each Rhumbix API endpoint.
Outputs a summary grouped by category.
"""
import logging
from datetime import datetime, timedelta

from src.config import API_KEY, BASE_URL

# Organizational Structure
from src.companies.api import get_companies
from src.company_groups.api import get_rhumbix_ou_list, get_company_groups_details
from src.company_classifications.api import get_company_classifications
from src.company_trades.api import get_company_trades
from src.groups.api import get_groups
from src.cohorts.api import get_cohorts

# People & Users
from src.employees.api import get_employees
from src.users.api import get_users
from src.employees_projects.api import get_employees_projects
from src.employees_groups.api import get_employees_groups
from src.employees_pricing.api import get_employees_pricing

# Projects & Work
from src.projects.api import get_projects
from src.field_folders.api import get_field_folders
from src.field_folder_notes.api import get_field_folder_notes
from src.change_orders.api import get_change_orders
from src.budgets.api import get_budgets

# Cost Tracking
from src.cost_codes.api import get_cost_codes
from src.cost_code_controls.api import get_cost_code_controls
from src.cost_items.api import get_cost_items

# Timekeeping
from src.timekeeping_entries.api import get_timekeeping_entries
from src.timekeeping_statuses.api import get_timekeeping_statuses
from src.deleted_timekeeping_entries.api import get_deleted_timekeeping_entries
from src.clock_entries.api import get_clock_in_clock_out_entries
from src.clock_timelines.api import get_clock_in_clock_out_timelines
from src.employee_shifts_and_breaks.api import get_employee_shifts_and_breaks
from src.work_shift_details.api import get_work_shift_details
from src.employee_shift_details.api import get_employee_shift_details
from src.locked_time_periods.api import get_locked_time_periods
from src.start_stop_types.api import get_start_stop_types

# Time Off & Absences
from src.absence_types.api import get_absence_types
from src.absences.api import get_absences
from src.timeoff_requests.api import get_timeoff_requests

# Equipment
from src.equipment.api import get_equipment
from src.equipment_pricing.api import get_equipment_pricing
from src.project_equipment.api import get_project_equipment

# Materials
from src.materials.api import get_materials
from src.material_pricing.api import get_material_pricing
from src.project_materials.api import get_project_materials

# Custom Data & Workflows
from src.picklists.api import get_picklists
from src.picklist_items.api import get_picklist_items
from src.shift_extra_schemas.api import get_shift_extra_schemas
from src.shift_extra_entries.api import get_shift_extra_entries
from src.workflow_entries.api import get_workflow_entries

# Other
from src.notes.api import get_notes
from src.quantity_entries.api import get_quantity_entries
from src.email_alerts.api import get_email_alerts

logging.basicConfig(level=logging.INFO, format='%(message)s')

def safe_count(func, **kwargs):
    """Safely call a function and return count or error message."""
    try:
        result = func(**kwargs)
        if result is None:
            return "Error"
        return len(result)
    except Exception as e:
        return f"Error: {str(e)[:30]}"

def main():
    if not API_KEY or "your_api_key_here" in API_KEY or not BASE_URL:
        logging.error("API_KEY or BASE_URL is not configured. Please check your .env file.")
        return

    # Date range for endpoints that require dates (last 365 days)
    end_date = datetime.utcnow().strftime("%Y-%m-%d")
    start_date = (datetime.utcnow() - timedelta(days=365)).strftime("%Y-%m-%d")

    print("\n" + "="*60)
    print("RHUMBIX API ENDPOINT DATA COUNT")
    print("="*60)

    # Organizational Structure
    print("\n--- ORGANIZATIONAL STRUCTURE ---")
    print(f"  companies:                {safe_count(get_companies)}")
    print(f"  company_groups (OU list): {safe_count(get_rhumbix_ou_list)}")
    print(f"  company_groups (details): {safe_count(get_company_groups_details)}")
    print(f"  company_classifications:  {safe_count(get_company_classifications)}")
    print(f"  company_trades:           {safe_count(get_company_trades)}")
    print(f"  groups:                   {safe_count(get_groups)}")
    print(f"  cohorts:                  {safe_count(get_cohorts)}")

    # People & Users
    print("\n--- PEOPLE & USERS ---")
    print(f"  employees:                {safe_count(get_employees)}")
    print(f"  users:                    {safe_count(get_users)}")
    print(f"  employees_projects:       {safe_count(get_employees_projects)}")
    print(f"  employees_groups:         {safe_count(get_employees_groups)}")
    print(f"  employees_pricing:        {safe_count(get_employees_pricing)}")

    # Projects & Work
    print("\n--- PROJECTS & WORK ---")
    print(f"  projects:                 {safe_count(get_projects)}")
    print(f"  field_folders:            {safe_count(get_field_folders)}")
    print(f"  field_folder_notes:       {safe_count(get_field_folder_notes)}")
    print(f"  change_orders:            {safe_count(get_change_orders)}")
    print(f"  budgets:                  {safe_count(get_budgets)}")

    # Cost Tracking
    print("\n--- COST TRACKING ---")
    print(f"  cost_codes:               {safe_count(get_cost_codes)}")
    print(f"  cost_code_controls:       {safe_count(get_cost_code_controls)}")
    print(f"  cost_items:               {safe_count(get_cost_items)}")

    # Timekeeping (some require date ranges)
    # For clock_entries, use start_time/end_time (datetime format)
    start_datetime = (datetime.utcnow() - timedelta(days=365)).isoformat() + "Z"
    end_datetime = datetime.utcnow().isoformat() + "Z"

    print("\n--- TIMEKEEPING ---")
    print(f"  timekeeping_entries (1yr):{safe_count(get_timekeeping_entries, start_date=start_date, end_date=end_date)}")
    print(f"  timekeeping_statuses:     {safe_count(get_timekeeping_statuses)}")
    print(f"  clock_entries (1yr):      {safe_count(get_clock_in_clock_out_entries, start_time=start_datetime, end_time=end_datetime)}")
    print(f"  clock_timelines (1yr):    {safe_count(get_clock_in_clock_out_timelines, start_date=start_date, end_date=end_date)}")
    print(f"  employee_shifts (1yr):    {safe_count(get_employee_shifts_and_breaks, start_date=start_date, end_date=end_date)}")
    print(f"  work_shift_details (1yr): {safe_count(get_work_shift_details, start_date=start_date, end_date=end_date)}")
    print(f"  employee_shift_details:   {safe_count(get_employee_shift_details, start_date=start_date, end_date=end_date)}")
    print(f"  locked_time_periods:      {safe_count(get_locked_time_periods)}")
    print(f"  start_stop_types:         {safe_count(get_start_stop_types)}")

    # Time Off & Absences
    print("\n--- TIME OFF & ABSENCES ---")
    print(f"  absence_types:            {safe_count(get_absence_types)}")
    print(f"  absences (1yr):           {safe_count(get_absences, start_date=start_date, end_date=end_date)}")
    print(f"  timeoff_requests (1yr):   {safe_count(get_timeoff_requests, start_date=start_date, end_date=end_date)}")

    # Equipment
    print("\n--- EQUIPMENT ---")
    print(f"  equipment:                {safe_count(get_equipment)}")
    print(f"  equipment_pricing:        {safe_count(get_equipment_pricing)}")
    print(f"  project_equipment:        {safe_count(get_project_equipment)}")

    # Materials
    print("\n--- MATERIALS ---")
    print(f"  materials:                {safe_count(get_materials)}")
    print(f"  material_pricing:         {safe_count(get_material_pricing)}")
    print(f"  project_materials:        {safe_count(get_project_materials)}")

    # Custom Data & Workflows
    print("\n--- CUSTOM DATA & WORKFLOWS ---")
    print(f"  picklists:                {safe_count(get_picklists)}")
    print(f"  picklist_items:           {safe_count(get_picklist_items)}")
    print(f"  shift_extra_schemas:      {safe_count(get_shift_extra_schemas)}")
    print(f"  shift_extra_entries (1yr):{safe_count(get_shift_extra_entries, start_date=start_date, end_date=end_date)}")
    print(f"  workflow_entries:         {safe_count(get_workflow_entries)}")

    # Other
    print("\n--- OTHER ---")
    print(f"  notes (1yr):              {safe_count(get_notes, start_date=start_date, end_date=end_date)}")
    print(f"  quantity_entries (1yr):   {safe_count(get_quantity_entries, start_date=start_date, end_date=end_date)}")
    print(f"  email_alerts:             {safe_count(get_email_alerts)}")

    print("\n" + "="*60)
    print("Note: (1yr) = data from the last 365 days")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
