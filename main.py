import logging
import os
from datetime import datetime, timedelta
import json
import pandas as pd

from src.company_groups.api import get_rhumbix_ou_list, get_company_groups_details
from src.absence_types.api import get_absence_types
from src.absences.api import get_absences
from src.budgets.api import get_budgets


from src.cohorts.api import get_cohorts
from src.companies.api import get_companies
from src.cost_codes.api import get_cost_codes
from src.employees.api import get_employees
from src.equipment.api import get_equipment
from src.field_folder_notes.api import get_field_folder_notes
from src.absences_history.api import get_absences_history
from src.timekeeping_entries.history.api import get_timekeeping_entries_history
from src.timekeeping_entries.api import get_timekeeping_entries
from src.deleted_timekeeping_entries.api import get_deleted_timekeeping_entries
from src.cost_code_controls.api import get_cost_code_controls
from src.company_classifications.api import get_company_classifications
from src.company_trades.api import get_company_trades
from src.change_orders.api import get_change_orders
from src.cost_items.api import get_cost_items
from src.employees_projects.api import get_employees_projects
from src.employees_groups.api import get_employees_groups
from src.employees_pricing.api import get_employees_pricing
from src.equipment_pricing.api import get_equipment_pricing
from src.materials.api import get_materials
from src.material_pricing.api import get_material_pricing
from src.project_equipment.api import get_project_equipment
from src.project_materials.api import get_project_materials
from src.picklists.api import get_picklists
from src.picklist_items.api import get_picklist_items
from src.shift_extra_schemas.api import get_shift_extra_schemas
from src.shift_extra_entries.api import get_shift_extra_entries
from src.shift_extra_entries_history.api import get_shift_extra_entries_history
from src.employee_shifts_and_breaks.api import get_employee_shifts_and_breaks
from src.employee_shifts_and_breaks_history.api import get_employee_shifts_and_breaks_history
from src.work_shift_details.api import get_work_shift_details
from src.employee_shift_details.api import get_employee_shift_details
from src.workflow_entries.api import get_workflow_entries
from src.workflow_entries_history.api import get_workflow_entries_history
from src.locked_time_periods.api import get_locked_time_periods
from src.notes.api import get_notes
from src.quantity_entries.api import get_quantity_entries
from src.email_alerts.api import get_email_alerts
from src.start_stop_types.api import get_start_stop_types
from src.config import API_KEY, BASE_URL

# Configure logging
logging.basicConfig(level=logging.INFO)

OUTPUT_DIR = "output"

def save_output(data, filename_prefix):
    """Saves data to JSON and CSV files in the 'output' directory."""
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    json_path = os.path.join(OUTPUT_DIR, f"{filename_prefix}.json")
    csv_path = os.path.join(OUTPUT_DIR, f"{filename_prefix}.csv")

    with open(json_path, 'w') as f:
        json.dump(data, f, indent=2)
    logging.info(f"JSON output saved to {json_path}")

    try:
        df = pd.json_normalize(data)
        df.to_csv(csv_path, index=False)
        logging.info(f"CSV output saved to {csv_path}")
    except Exception as e:
        logging.error(f"Could not save CSV file: {e}")

def run_tests():
    """
    Main function to test Rhumbix API calls.
    Uncomment specific test blocks to run them. Output is saved to the 'output' directory.
    """
    if not API_KEY or "your_api_key_here" in API_KEY or not BASE_URL:
        logging.error("API_KEY or BASE_URL is not configured. Please check your .env file.")
        return

    logging.info("Rhumbix API Test Runner started.")
    logging.info("Uncomment a test block to run it.")

    # =================================================================
    # ================= COMPANY GROUPS API CALLS ======================
    # =================================================================

    # --- Test get_rhumbix_ou_list (simple list) ---
    # Uncomment to run:
    # ou_list = get_rhumbix_ou_list()
    # if ou_list:
    #     save_output(ou_list, "ou_list")
    # else:
    #     logging.error("Failed to fetch OU list.")

    # --- Test get_company_groups_details (all parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # seven_days_ago = (datetime.utcnow() - timedelta(days=7)).isoformat() + "Z"
    # detailed_groups_all_params = get_company_groups_details(
    #     last_updated=seven_days_ago,
    #     page_size=10
    # )
    # if detailed_groups_all_params:
    #     save_output(detailed_groups_all_params, "company_groups_detailed_all_params")
    # else:
    #     logging.error("Failed to fetch detailed company groups with all params.")

    # --- Test get_company_groups_details (date parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # thirty_days_ago = (datetime.utcnow() - timedelta(days=30)).isoformat() + "Z"
    # detailed_groups_date_params = get_company_groups_details(
    #     last_updated=thirty_days_ago
    # )
    # if detailed_groups_date_params:
    #     save_output(detailed_groups_date_params, "company_groups_detailed_date_params")
    # else:
    #     logging.error("Failed to fetch detailed company groups with date params.")

    # =================================================================
    # ================ ABSENCE TYPES API CALLS ========================
    # =================================================================

    # --- Test get_absence_types (all parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # absence_types_all_params = get_absence_types(
    #     page_size=5
    # )
    # if absence_types_all_params:
    #     save_output(absence_types_all_params, "absence_types_all_params")
    # else:
    #     logging.error("Failed to fetch absence types with all params.")

    # =================================================================
    # =================== ABSENCES API CALLS ==========================
    # =================================================================

    # --- Test get_absences (all parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # start_date_absences_all = "2023-01-01"
    # end_date_absences_all = "2023-01-31"
    # last_updated_absences_all = (datetime.utcnow() - timedelta(days=60)).isoformat() + "Z"
    # absences_all_params = get_absences(
    #     page_size=10,
    #     start_date=start_date_absences_all,
    #     end_date=end_date_absences_all,
    #     is_approved=True,
    #     status="APPROVED",
    #     employee="SOME_EMPLOYEE_ID", # CHANGE THIS
    #     last_updated=last_updated_absences_all,
    #     include_deleted=False,
    #     group_id=[123, 456], # CHANGE THIS
    #     include_subgroups=True
    # )
    # if absences_all_params:
    #     save_output(absences_all_params, "absences_all_params")
    # else:
    #     logging.error("Failed to fetch absences with all params.")

    # --- Test get_absences (date parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # start_date_absences_date = "2023-02-01"
    # end_date_absences_date = "2023-02-28"
    # absences_date_params = get_absences(
    #     start_date=start_date_absences_date,
    #     end_date=end_date_absences_date
    # )
    # if absences_date_params:
    #     save_output(absences_date_params, "absences_date_params")
    # else:
    #     logging.error("Failed to fetch absences with date params.")

    # =================================================================
    # ==================== BUDGETS API CALLS ==========================
    # =================================================================

    # --- Test get_budgets (all parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # last_updated_budgets_all = (datetime.utcnow() - timedelta(days=90)).isoformat() + "Z"
    # budgets_all_params = get_budgets(
    #     page_size=20,
    #     job_number="SOME_JOB_NUMBER", # CHANGE THIS
    #     source="FIELD",
    #     last_updated=last_updated_budgets_all,
    #     cost_code="SOME_COST_CODE" # CHANGE THIS
    # )
    # if budgets_all_params:
    #     save_output(budgets_all_params, "budgets_all_params")
    # else:
    #     logging.error("Failed to fetch budgets with all params.")

    # --- Test get_budgets (date parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # last_updated_budgets_date = (datetime.utcnow() - timedelta(days=120)).isoformat() + "Z"
    # budgets_date_params = get_budgets(
    #     last_updated=last_updated_budgets_date
    # )
    # if budgets_date_params:
    #     save_output(budgets_date_params, "budgets_date_params")
    # else:
    #     logging.error("Failed to fetch budgets with date params.")



    # =================================================================
    # =========== CLOCK IN/OUT TIMELINES API CALLS ====================
    # =================================================================

    # --- Test get_clock_in_clock_out_timelines (all parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # start_date_timelines_all = "2023-03-01"
    # end_date_timelines_all = "2023-03-31"
    # clock_timelines_all_params = get_clock_in_clock_out_timelines(
    #     page_size=5,
    #     foreman=["FOREMAN_ID_1"], # CHANGE THIS
    #     start_date=start_date_timelines_all,
    #     end_date=end_date_timelines_all,
    #     job_number=["JOB_NUM_1"], # CHANGE THIS
    #     worker=["WORKER_ID_A"] # CHANGE THIS
    # )
    # if clock_timelines_all_params:
    #     save_output(clock_timelines_all_params, "clock_timelines_all_params")
    # else:
    #     logging.error("Failed to fetch clock timelines with all params.")

    # --- Test get_clock_in_clock_out_timelines (date parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # start_date_timelines_date = "2023-04-01"
    # end_date_timelines_date = "2023-04-30"
    # clock_timelines_date_params = get_clock_in_clock_out_timelines(
    #     start_date=start_date_timelines_date,
    #     end_date=end_date_timelines_date
    # )
    # if clock_timelines_date_params:
    #     save_output(clock_timelines_date_params, "clock_timelines_date_params")
    # else:
    #     logging.error("Failed to fetch clock timelines with date params.")

    # =================================================================
    # ===================== COHORTS API CALLS =========================
    # =================================================================

    # --- Test get_cohorts (all parameters & custom field) ---
    # Uncomment to run (adjust parameters as needed):
    # last_updated_cohorts_all = (datetime.utcnow() - timedelta(days=180)).isoformat() + "Z"
    # cohorts_all_params = get_cohorts(
    #     page_size=15,
    #     last_updated=last_updated_cohorts_all,
    #     custom_field_zone_id="12345"  # CHANGE THIS: example custom field
    # )
    # if cohorts_all_params:
    #     save_output(cohorts_all_params, "cohorts_all_params")
    # else:
    #     logging.error("Failed to fetch cohorts with all params.")

    # --- Test get_cohorts (date parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # last_updated_cohorts_date = (datetime.utcnow() - timedelta(days=200)).isoformat() + "Z"
    # cohorts_date_params = get_cohorts(
    #     last_updated=last_updated_cohorts_date
    # )
    # if cohorts_date_params:
    #     save_output(cohorts_date_params, "cohorts_date_params")
    # else:
    #     logging.error("Failed to fetch cohorts with date params.")

    # =================================================================
    # ===================== COMPANIES API CALLS =======================
    # =================================================================

    # --- Test get_companies (all parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # companies_all_params = get_companies(
    #     page_size=10,
    #     job_number="SOME_JOB_NUMBER" # CHANGE THIS
    # )
    # if companies_all_params:
    #     save_output(companies_all_params, "companies_all_params")
    # else:
    #     logging.error("Failed to fetch companies with all params.")
        
    # =================================================================
    # ===================== COST CODES API CALLS ======================
    # =================================================================

    # --- Test get_cost_codes (all parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # last_updated_codes_all = (datetime.utcnow() - timedelta(days=10)).isoformat() + "Z"
    # cost_codes_all_params = get_cost_codes(
    #     page_size=25,
    #     job_number=["JOB_NUM_1", "JOB_NUM_2"], # CHANGE THIS
    #     last_updated=last_updated_codes_all,
    #     is_active=True,
    #     code="SOME_CODE", # CHANGE THIS
    #     description="some description", # CHANGE THIS
    #     has_budgets=True,
    #     include_deleted=False,
    #     custom_field_example="some_value" # CHANGE THIS
    # )
    # if cost_codes_all_params:
    #     save_output(cost_codes_all_params, "cost_codes_all_params")
    # else:
    #     logging.error("Failed to fetch cost codes with all params.")

    # --- Test get_cost_codes (date parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # last_updated_codes_date = (datetime.utcnow() - timedelta(days=20)).isoformat() + "Z"
    # cost_codes_date_params = get_cost_codes(
    #     last_updated=last_updated_codes_date
    # )
    # if cost_codes_date_params:
    #     save_output(cost_codes_date_params, "cost_codes_date_params")
    # else:
    #     logging.error("Failed to fetch cost codes with date params.")

    # =================================================================
    # ===================== EMPLOYEES API CALLS =======================
    # =================================================================

    # --- Test get_employees (all parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # last_updated_employees_all = (datetime.utcnow() - timedelta(days=45)).isoformat() + "Z"
    # employees_all_params = get_employees(
    #     page_size=50,
    #     last_updated=last_updated_employees_all,
    #     is_active=True,
    #     company_supplied_id=["ID1", "ID2"], # CHANGE THIS
    #     group_id=[10, 20], # CHANGE THIS
    #     include_subgroups=True,
    #     email_address="employee@example.com", # CHANGE THIS
    #     phone_number="1234567890", # CHANGE THIS
    #     include_deleted=False
    # )
    # if employees_all_params:
    #     save_output(employees_all_params, "employees_all_params")
    # else:
    #     logging.error("Failed to fetch employees with all params.")

    # --- Test get_employees (date parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # last_updated_employees_date = (datetime.utcnow() - timedelta(days=90)).isoformat() + "Z"
    # employees_date_params = get_employees(
    #     last_updated=last_updated_employees_date
    # )
    # if employees_date_params:
    #     save_output(employees_date_params, "employees_date_params")
    # else:
    #     logging.error("Failed to fetch employees with date params.")
        
    # =================================================================
    # ===================== EQUIPMENT API CALLS =======================
    # =================================================================

    # --- Test get_equipment (all parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # last_updated_equipment_all = (datetime.utcnow() - timedelta(days=50)).isoformat() + "Z"
    # equipment_all_params = get_equipment(
    #     page_size=10,
    #     last_updated=last_updated_equipment_all,
    #     name="Excavator", # CHANGE THIS
    #     is_active=True,
    #     equipment_category=[1, 2], # CHANGE THIS
    #     include_deleted=False
    # )
    # if equipment_all_params:
    #     save_output(equipment_all_params, "equipment_all_params")
    # else:
    #     logging.error("Failed to fetch equipment with all params.")

    # --- Test get_equipment (date parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # last_updated_equipment_date = (datetime.utcnow() - timedelta(days=100)).isoformat() + "Z"
    # equipment_date_params = get_equipment(
    #     last_updated=last_updated_equipment_date
    # )
    # if equipment_date_params:
    #     save_output(equipment_date_params, "equipment_date_params")
    # else:
    #     logging.error("Failed to fetch equipment with date params.")

    # =================================================================
    # ================= FIELD FOLDER NOTES API CALLS ==================
    # =================================================================

    # --- Test get_field_folder_notes (all parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # ffn_all_params = get_field_folder_notes(
    #     page_size=5,
    #     project=[1, 2], # CHANGE THIS
    #     author=[101, 102], # CHANGE THIS
    #     shift_date_from="2023-01-01",
    #     shift_date_to="2023-01-31",
    #     created_on_from=(datetime.utcnow() - timedelta(days=30)).isoformat() + "Z",
    #     created_on_to=datetime.utcnow().isoformat() + "Z",
    #     last_updated_from=(datetime.utcnow() - timedelta(days=7)).isoformat() + "Z",
    #     last_updated_to=datetime.utcnow().isoformat() + "Z",
    #     is_private=False,
    #     is_daily_report=True,
    #     has_photos=True,
    #     has_files=False,
    #     has_weather=True,
    #     has_delays=False,
    #     has_visitors=True,
    #     has_tags=True,
    #     tags=["tag1", "tag2"], # CHANGE THIS
    #     cost_codes=["CC1", "CC2"], # CHANGE THIS
    #     equipment=[201, 202], # CHANGE THIS
    #     employees=["EMP1", "EMP2"], # CHANGE THIS
    #     note_type=["type1", "type2"], # CHANGE THIS
    #     include_deleted=False
    # )
    # if ffn_all_params:
    #     save_output(ffn_all_params, "field_folder_notes_all_params")
    # else:
    #     logging.error("Failed to fetch field folder notes with all params.")

    # --- Test get_field_folder_notes (date parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # ffn_date_params = get_field_folder_notes(
    #     shift_date_from="2023-02-01",
    #     shift_date_to="2023-02-28",
    #     last_updated_from=(datetime.utcnow() - timedelta(days=10)).isoformat() + "Z"
    # )
    # if ffn_date_params:
    #     save_output(ffn_date_params, "field_folder_notes_date_params")
    # else:
    #     logging.error("Failed to fetch field folder notes with date params.")

    # else:
    #     logging.error("Failed to fetch field folder notes with date params.")

    # =================================================================
    # ================= ABSENCES HISTORY API CALLS ====================
    # =================================================================

    # --- Test get_absences_history (all parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # history_start_date = (datetime.utcnow() - timedelta(days=90)).isoformat() + "Z"
    # history_end_date = datetime.utcnow().isoformat() + "Z"
    # absences_history_all_params = get_absences_history(
    #     page_size=10,
    #     ids=[123, 456],  # CHANGE THIS
    #     history_start_date=history_start_date,
    #     history_end_date=history_end_date,
    #     history_type="UPDATED"  # CHANGE THIS (e.g., "CREATED", "UPDATED", "DELETED")
    # )
    # if absences_history_all_params:
    #     save_output(absences_history_all_params, "absences_history_all_params")
    # else:
    #     logging.error("Failed to fetch absence history with all params.")

    # --- Test get_absences_history (date parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # history_start_date_only = (datetime.utcnow() - timedelta(days=60)).isoformat() + "Z"
    # absences_history_date_params = get_absences_history(
    #     history_start_date=history_start_date_only
    # )
    # if absences_history_date_params:
    #     save_output(absences_history_date_params, "absences_history_date_params")
    # else:
    #     logging.error("Failed to fetch absence history with date params.")

    # else:
    #     logging.error("Failed to fetch absence history with date params.")

    # =================================================================
    # =============== TIMEKEEPING ENTRIES HISTORY API CALLS =============
    # =================================================================

    # --- Test get_timekeeping_entries_history (all parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # history_start_date_tkh = (datetime.utcnow() - timedelta(days=90)).isoformat() + "Z"
    # history_end_date_tkh = datetime.utcnow().isoformat() + "Z"
    # timekeeping_history_all_params = get_timekeeping_entries_history(
    #     page_size=10,
    #     ids=[123, 456],  # CHANGE THIS
    #     history_start_date=history_start_date_tkh,
    #     history_end_date=history_end_date_tkh,
    #     history_type="UPDATED"  # CHANGE THIS (e.g., "CREATED", "UPDATED", "DELETED")
    # )
    # if timekeeping_history_all_params:
    #     save_output(timekeeping_history_all_params, "timekeeping_history_all_params")
    # else:
    #     logging.error("Failed to fetch timekeeping history with all params.")

    # --- Test get_timekeeping_entries_history (date parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # history_start_date_only_tkh = (datetime.utcnow() - timedelta(days=60)).isoformat() + "Z"
    # timekeeping_history_date_params = get_timekeeping_entries_history(
    #     history_start_date=history_start_date_only_tkh
    # )
    # if timekeeping_history_date_params:
    #     save_output(timekeeping_history_date_params, "timekeeping_history_date_params")
    # else:
    #     logging.error("Failed to fetch timekeeping history with date params.")

    # else:
    #     logging.error("Failed to fetch timekeeping history with date params.")

    # =================================================================
    # =============== DELETED TIMEKEEPING ENTRIES API CALLS =============
    # =================================================================

    # --- Test get_deleted_timekeeping_entries (all parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # deleted_history_start_date = (datetime.utcnow() - timedelta(days=90)).isoformat() + "Z"
    # deleted_history_end_date = datetime.utcnow().isoformat() + "Z"
    # deleted_timekeeping_all_params = get_deleted_timekeeping_entries(
    #     history_start_date=deleted_history_start_date,
    #     history_end_date=deleted_history_end_date,
    # )
    # if deleted_timekeeping_all_params:
    #     save_output(deleted_timekeeping_all_params, "deleted_timekeeping_all_params")
    # else:
    #     logging.error("Failed to fetch deleted timekeeping entries with all params.")

    # --- Test get_deleted_timekeeping_entries (date parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # deleted_history_start_date_only = (datetime.utcnow() - timedelta(days=60)).isoformat() + "Z"
    # deleted_timekeeping_date_params = get_deleted_timekeeping_entries(
    #     history_start_date=deleted_history_start_date_only
    # )
    # if deleted_timekeeping_date_params:
    #     save_output(deleted_timekeeping_date_params, "deleted_timekeeping_date_params")
    # else:
    #     logging.error("Failed to fetch deleted timekeeping entries with date params.")

    # else:
    #     logging.error("Failed to fetch deleted timekeeping entries with date params.")

    # =================================================================
    # ================= COST CODE CONTROLS API CALLS ==================
    # =================================================================

    # --- Test get_cost_code_controls (all parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # cost_code_controls_all_params = get_cost_code_controls(
    #     page_size=10,
    #     is_active=True,
    #     labor_type="SOME_LABOR_TYPE", # CHANGE THIS
    #     cost_code_type="SOME_COST_CODE_TYPE", # CHANGE THIS
    # )
    # if cost_code_controls_all_params:
    #     save_output(cost_code_controls_all_params, "cost_code_controls_all_params")
    # else:
    #     logging.error("Failed to fetch cost code controls with all params.")

    # --- Test get_cost_code_controls (simple list) ---
    # Uncomment to run:
    # cost_code_controls_list = get_cost_code_controls()
    # if cost_code_controls_list:
    #     save_output(cost_code_controls_list, "cost_code_controls_list")
    # else:
    #     logging.error("Failed to fetch cost code controls list.")
        
    # =================================================================
    # =============== COMPANY CLASSIFICATIONS API CALLS ===============
    # =================================================================

    # --- Test get_company_classifications (all parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # company_classifications_all_params = get_company_classifications(
    #     page_size=5
    # )
    # if company_classifications_all_params:
    #     save_output(company_classifications_all_params, "company_classifications_all_params")
    # else:
    #     logging.error("Failed to fetch company classifications with all params.")

    # --- Test get_company_classifications (simple list) ---
    # Uncomment to run:
    # company_classifications_list = get_company_classifications()
    # if company_classifications_list:
    #     save_output(company_classifications_list, "company_classifications_list")
    # else:
    #     logging.error("Failed to fetch company classifications list.")

    # else:
    #     logging.error("Failed to fetch company classifications list.")

    # =================================================================
    # ================= COMPANY TRADES API CALLS ======================
    # =================================================================

    # --- Test get_company_trades (all parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # company_trades_all_params = get_company_trades(
    #     page_size=5
    # )
    # if company_trades_all_params:
    #     save_output(company_trades_all_params, "company_trades_all_params")
    # else:
    #     logging.error("Failed to fetch company trades with all params.")

    # --- Test get_company_trades (simple list) ---
    # Uncomment to run:
    # company_trades_list = get_company_trades()
    # if company_trades_list:
    #     save_output(company_trades_list, "company_trades_list")
    # else:
    #     logging.error("Failed to fetch company trades list.")

    # else:
    #     logging.error("Failed to fetch company trades list.")

    # =================================================================
    # =================== CHANGE ORDERS API CALLS =====================
    # =================================================================

    # --- Test get_change_orders (all parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # last_updated_change_orders = (datetime.utcnow() - timedelta(days=30)).isoformat() + "Z"
    # change_orders_all_params = get_change_orders(
    #     page_size=10,
    #     job_number="SOME_JOB_NUMBER", # CHANGE THIS
    #     is_active=True,
    #     last_updated=last_updated_change_orders
    # )
    # if change_orders_all_params:
    #     save_output(change_orders_all_params, "change_orders_all_params")
    # else:
    #     logging.error("Failed to fetch change orders with all params.")

    # --- Test get_change_orders (simple list) ---
    # Uncomment to run:
    # change_orders_list = get_change_orders()
    # if change_orders_list:
    #     save_output(change_orders_list, "change_orders_list")
    # else:
    #     logging.error("Failed to fetch change orders list.")
    # else:
    #     logging.error("Failed to fetch change orders list.")
    
    # =================================================================
    # ===================== COST ITEMS API CALLS ======================
    # =================================================================

    # --- Test get_cost_items (all parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # last_updated_cost_items = (datetime.utcnow() - timedelta(days=30)).isoformat() + "Z"
    # cost_items_all_params = get_cost_items(
    #     page_size=10,
    #     job_number="SOME_JOB_NUMBER", # CHANGE THIS
    #     change_order_key="SOME_CHANGE_ORDER_KEY", # CHANGE THIS
    #     is_active=True,
    #     last_updated=last_updated_cost_items
    # )
    # if cost_items_all_params:
    #     save_output(cost_items_all_params, "cost_items_all_params")
    # else:
    #     logging.error("Failed to fetch cost items with all params.")

    # --- Test get_cost_items (simple list) ---
    # Uncomment to run:
    # cost_items_list = get_cost_items()
    # if cost_items_list:
    #     save_output(cost_items_list, "cost_items_list")
    # else:
    #     logging.error("Failed to fetch cost items list.")

    # else:
    #     logging.error("Failed to fetch cost items list.")

    # =================================================================
    # =================== EMPLOYEES PROJECTS API CALLS ==================
    # =================================================================

    # --- Test get_employees_projects (all parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # employees_projects_all_params = get_employees_projects(
    #     page_size=10,
    #     employees=["EMP1", "EMP2"], # CHANGE THIS
    #     job_numbers=["JOB1", "JOB2"], # CHANGE THIS
    # )
    # if employees_projects_all_params:
    #     save_output(employees_projects_all_params, "employees_projects_all_params")
    # else:
    #     logging.error("Failed to fetch employees_projects with all params.")

    # --- Test get_employees_projects (simple list) ---
    # Uncomment to run:
    # employees_projects_list = get_employees_projects()
    # if employees_projects_list:
    #     save_output(employees_projects_list, "employees_projects_list")
    # else:
    #     logging.error("Failed to fetch employees_projects list.")

    # else:
    #     logging.error("Failed to fetch employees_projects list.")

    # =================================================================
    # =================== EMPLOYEES GROUPS API CALLS ==================
    # =================================================================

    # --- Test get_employees_groups (all parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # employees_groups_all_params = get_employees_groups(
    #     page_size=10,
    #     employees=["EMP1", "EMP2"], # CHANGE THIS
    #     groups=["GROUP1", "GROUP2"], # CHANGE THIS
    # )
    # if employees_groups_all_params:
    #     save_output(employees_groups_all_params, "employees_groups_all_params")
    # else:
    #     logging.error("Failed to fetch employees_groups with all params.")

    # --- Test get_employees_groups (simple list) ---
    # Uncomment to run:
    # employees_groups_list = get_employees_groups()
    # if employees_groups_list:
    #     save_output(employees_groups_list, "employees_groups_list")
    # else:
    #     logging.error("Failed to fetch employees_groups list.")

    # else:
    #     logging.error("Failed to fetch employees_groups list.")

    # =================================================================
    # ================= EMPLOYEES PRICING API CALLS ===================
    # =================================================================

    # --- Test get_employees_pricing (all parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # employees_pricing_all_params = get_employees_pricing(
    #     page_size=10,
    #     employees=["EMP1", "EMP2"], # CHANGE THIS
    # )
    # if employees_pricing_all_params:
    #     save_output(employees_pricing_all_params, "employees_pricing_all_params")
    # else:
    #     logging.error("Failed to fetch employees_pricing with all params.")

    # --- Test get_employees_pricing (simple list) ---
    # Uncomment to run:
    # employees_pricing_list = get_employees_pricing()
    # if employees_pricing_list:
    #     save_output(employees_pricing_list, "employees_pricing_list")
    # else:
    #     logging.error("Failed to fetch employees_pricing list.")

    # else:
    #     logging.error("Failed to fetch employees_pricing list.")

    # =================================================================
    # ================= EQUIPMENT PRICING API CALLS ===================
    # =================================================================

    # --- Test get_equipment_pricing (all parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # equipment_pricing_all_params = get_equipment_pricing(
    #     page_size=10,
    #     equipment=["EQUIP1", "EQUIP2"], # CHANGE THIS
    # )
    # if equipment_pricing_all_params:
    #     save_output(equipment_pricing_all_params, "equipment_pricing_all_params")
    # else:
    #     logging.error("Failed to fetch equipment_pricing with all params.")

    # --- Test get_equipment_pricing (simple list) ---
    # Uncomment to run:
    # equipment_pricing_list = get_equipment_pricing()
    # if equipment_pricing_list:
    #     save_output(equipment_pricing_list, "equipment_pricing_list")
    # else:
    #     logging.error("Failed to fetch equipment_pricing list.")

    # else:
    #     logging.error("Failed to fetch equipment_pricing list.")

    # =================================================================
    # ===================== MATERIALS API CALLS =======================
    # =================================================================

    # --- Test get_materials (all parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # last_updated_materials = (datetime.utcnow() - timedelta(days=30)).isoformat() + "Z"
    # materials_all_params = get_materials(
    #     page_size=10,
    #     last_updated=last_updated_materials,
    #     is_active=True
    # )
    # if materials_all_params:
    #     save_output(materials_all_params, "materials_all_params")
    # else:
    #     logging.error("Failed to fetch materials with all params.")

    # --- Test get_materials (simple list) ---
    # Uncomment to run:
    # materials_list = get_materials()
    # if materials_list:
    #     save_output(materials_list, "materials_list")
    # else:
    #     logging.error("Failed to fetch materials list.")

    # else:
    #     logging.error("Failed to fetch materials list.")

    # =================================================================
    # =================== MATERIAL PRICING API CALLS ==================
    # =================================================================

    # --- Test get_material_pricing (all parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # material_pricing_all_params = get_material_pricing(
    #     page_size=10,
    #     materials=["MAT1", "MAT2"], # CHANGE THIS
    # )
    # if material_pricing_all_params:
    #     save_output(material_pricing_all_params, "material_pricing_all_params")
    # else:
    #     logging.error("Failed to fetch material_pricing with all params.")

    # --- Test get_material_pricing (simple list) ---
    # Uncomment to run:
    # material_pricing_list = get_material_pricing()
    # if material_pricing_list:
    #     save_output(material_pricing_list, "material_pricing_list")
    # else:
    #     logging.error("Failed to fetch material_pricing list.")

    # else:
    #     logging.error("Failed to fetch material_pricing list.")

    # =================================================================
    # =================== PROJECT EQUIPMENT API CALLS =================
    # =================================================================

    # --- Test get_project_equipment (all parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # project_equipment_all_params = get_project_equipment(
    #     page_size=10,
    #     equipment=["EQUIP1", "EQUIP2"], # CHANGE THIS
    #     job_numbers=["JOB1", "JOB2"], # CHANGE THIS
    # )
    # if project_equipment_all_params:
    #     save_output(project_equipment_all_params, "project_equipment_all_params")
    # else:
    #     logging.error("Failed to fetch project_equipment with all params.")

    # --- Test get_project_equipment (simple list) ---
    # Uncomment to run:
    # project_equipment_list = get_project_equipment()
    # if project_equipment_list:
    #     save_output(project_equipment_list, "project_equipment_list")
    # else:
    #     logging.error("Failed to fetch project_equipment list.")

    # else:
    #     logging.error("Failed to fetch project_equipment list.")

    # =================================================================
    # ================== PROJECT MATERIALS API CALLS ==================
    # =================================================================

    # --- Test get_project_materials (all parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # project_materials_all_params = get_project_materials(
    #     page_size=10,
    #     materials=["MAT1", "MAT2"], # CHANGE THIS
    #     job_numbers=["JOB1", "JOB2"], # CHANGE THIS
    # )
    # if project_materials_all_params:
    #     save_output(project_materials_all_params, "project_materials_all_params")
    # else:
    #     logging.error("Failed to fetch project_materials with all params.")

    # --- Test get_project_materials (simple list) ---
    # Uncomment to run:
    # project_materials_list = get_project_materials()
    # if project_materials_list:
    #     save_output(project_materials_list, "project_materials_list")
    # else:
    #     logging.error("Failed to fetch project_materials list.")

    # else:
    #     logging.error("Failed to fetch project_materials list.")

    # =================================================================
    # ====================== PICKLISTS API CALLS ======================
    # =================================================================

    # --- Test get_picklists (all parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # last_updated_picklists = (datetime.utcnow() - timedelta(days=30)).isoformat() + "Z"
    # picklists_all_params = get_picklists(
    #     page_size=10,
    #     is_active=True,
    #     last_updated=last_updated_picklists
    # )
    # if picklists_all_params:
    #     save_output(picklists_all_params, "picklists_all_params")
    # else:
    #     logging.error("Failed to fetch picklists with all params.")

    # --- Test get_picklists (simple list) ---
    # Uncomment to run:
    # picklists_list = get_picklists()
    # if picklists_list:
    #     save_output(picklists_list, "picklists_list")
    # else:
    #     logging.error("Failed to fetch picklists list.")

    # else:
    #     logging.error("Failed to fetch picklists list.")

    # =================================================================
    # ==================== PICKLIST ITEMS API CALLS ===================
    # =================================================================

    # --- Test get_picklist_items (all parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # last_updated_picklist_items = (datetime.utcnow() - timedelta(days=30)).isoformat() + "Z"
    # picklist_items_all_params = get_picklist_items(
    #     page_size=10,
    #     is_active=True,
    #     last_updated=last_updated_picklist_items,
    #     picklist="SOME_PICKLIST" # CHANGE THIS
    # )
    # if picklist_items_all_params:
    #     save_output(picklist_items_all_params, "picklist_items_all_params")
    # else:
    #     logging.error("Failed to fetch picklist_items with all params.")

    # --- Test get_picklist_items (simple list) ---
    # Uncomment to run:
    # picklist_items_list = get_picklist_items()
    # if picklist_items_list:
    #     save_output(picklist_items_list, "picklist_items_list")
    # else:
    #     logging.error("Failed to fetch picklist_items list.")

    # else:
    #     logging.error("Failed to fetch picklist_items list.")

    # =================================================================
    # ================= SHIFT EXTRA SCHEMAS API CALLS =================
    # =================================================================

    # --- Test get_shift_extra_schemas (all parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # shift_extra_schemas_all_params = get_shift_extra_schemas(
    #     page_size=5
    # )
    # if shift_extra_schemas_all_params:
    #     save_output(shift_extra_schemas_all_params, "shift_extra_schemas_all_params")
    # else:
    #     logging.error("Failed to fetch shift_extra_schemas with all params.")

    # --- Test get_shift_extra_schemas (simple list) ---
    # Uncomment to run:
    # shift_extra_schemas_list = get_shift_extra_schemas()
    # if shift_extra_schemas_list:
    #     save_output(shift_extra_schemas_list, "shift_extra_schemas_list")
    # else:
    #     logging.error("Failed to fetch shift_extra_schemas list.")

    # else:
    #     logging.error("Failed to fetch shift_extra_schemas list.")

    # =================================================================
    # ================= SHIFT EXTRA ENTRIES API CALLS =================
    # =================================================================

    # --- Test get_shift_extra_entries (all parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # last_updated_shift_extra_entries = (datetime.utcnow() - timedelta(days=30)).isoformat() + "Z"
    # shift_extra_entries_all_params = get_shift_extra_entries(
    #     page_size=10,
    #     job_number="SOME_JOB_NUMBER", # CHANGE THIS
    #     start_date="2023-01-01", # CHANGE THIS
    #     end_date="2023-01-31", # CHANGE THIS
    #     is_approved=True,
    #     status="APPROVED",
    #     employee="SOME_EMPLOYEE_ID", # CHANGE THIS
    #     last_updated=last_updated_shift_extra_entries,
    #     is_active=True,
    #     work_shift_keys=[1,2,3], # CHANGE THIS
    #     include_deleted=False
    # )
    # if shift_extra_entries_all_params:
    #     save_output(shift_extra_entries_all_params, "shift_extra_entries_all_params")
    # else:
    #     logging.error("Failed to fetch shift_extra_entries with all params.")

    # --- Test get_shift_extra_entries (simple list) ---
    # Uncomment to run:
    # shift_extra_entries_list = get_shift_extra_entries()
    # if shift_extra_entries_list:
    #     save_output(shift_extra_entries_list, "shift_extra_entries_list")
    # else:
    #     logging.error("Failed to fetch shift_extra_entries list.")

    # else:
    #     logging.error("Failed to fetch shift_extra_entries list.")

    # =================================================================
    # ============== SHIFT EXTRA ENTRIES HISTORY API CALLS ============
    # =================================================================

    # --- Test get_shift_extra_entries_history (all parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # history_start_date_seeh = (datetime.utcnow() - timedelta(days=90)).isoformat() + "Z"
    # history_end_date_seeh = datetime.utcnow().isoformat() + "Z"
    # shift_extra_entries_history_all_params = get_shift_extra_entries_history(
    #     page_size=10,
    #     ids=[123, 456],  # CHANGE THIS
    #     history_start_date=history_start_date_seeh,
    #     history_end_date=history_end_date_seeh,
    #     history_type="UPDATED"  # CHANGE THIS (e.g., "CREATED", "UPDATED", "DELETED")
    # )
    # if shift_extra_entries_history_all_params:
    #     save_output(shift_extra_entries_history_all_params, "shift_extra_entries_history_all_params")
    # else:
    #     logging.error("Failed to fetch shift_extra_entries_history with all params.")

    # --- Test get_shift_extra_entries_history (date parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # history_start_date_only_seeh = (datetime.utcnow() - timedelta(days=60)).isoformat() + "Z"
    # shift_extra_entries_history_date_params = get_shift_extra_entries_history(
    #     history_start_date=history_start_date_only_seeh
    # )
    # if shift_extra_entries_history_date_params:
    #     save_output(shift_extra_entries_history_date_params, "shift_extra_entries_history_date_params")
    # else:
    #     logging.error("Failed to fetch shift_extra_entries_history with date params.")

    # else:
    #     logging.error("Failed to fetch shift_extra_entries_history with date params.")

    # =================================================================
    # ============= EMPLOYEE SHIFTS AND BREAKS API CALLS ==============
    # =================================================================

    # --- Test get_employee_shifts_and_breaks (all parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # last_updated_shifts = (datetime.utcnow() - timedelta(days=30)).isoformat() + "Z"
    # employee_shifts_and_breaks_all_params = get_employee_shifts_and_breaks(
    #     page_size=10,
    #     employee="SOME_EMPLOYEE_ID", # CHANGE THIS
    #     end_date="2023-01-31", # CHANGE THIS
    #     is_approved=True,
    #     last_updated=last_updated_shifts,
    #     start_date="2023-01-01", # CHANGE THIS
    #     status="APPROVED",
    #     work_shift_keys=[1,2,3], # CHANGE THIS
    #     include_deleted=False
    # )
    # if employee_shifts_and_breaks_all_params:
    #     save_output(employee_shifts_and_breaks_all_params, "employee_shifts_and_breaks_all_params")
    # else:
    #     logging.error("Failed to fetch employee_shifts_and_breaks with all params.")

    # --- Test get_employee_shifts_and_breaks (simple list) ---
    # Uncomment to run:
    # employee_shifts_and_breaks_list = get_employee_shifts_and_breaks()
    # if employee_shifts_and_breaks_list:
    #     save_output(employee_shifts_and_breaks_list, "employee_shifts_and_breaks_list")
    # else:
    #     logging.error("Failed to fetch employee_shifts_and_breaks list.")

    # else:
    #     logging.error("Failed to fetch employee_shifts_and_breaks list.")

    # =================================================================
    # ============ EMPLOYEE SHIFTS AND BREAKS HISTORY API CALLS =======
    # =================================================================

    # --- Test get_employee_shifts_and_breaks_history (all parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # history_start_date_esabh = (datetime.utcnow() - timedelta(days=90)).isoformat() + "Z"
    # history_end_date_esabh = datetime.utcnow().isoformat() + "Z"
    # employee_shifts_and_breaks_history_all_params = get_employee_shifts_and_breaks_history(
    #     page_size=10,
    #     ids=[123, 456],  # CHANGE THIS
    #     history_start_date=history_start_date_esabh,
    #     history_end_date=history_end_date_esabh,
    #     history_type="UPDATED"  # CHANGE THIS (e.g., "CREATED", "UPDATED", "DELETED")
    # )
    # if employee_shifts_and_breaks_history_all_params:
    #     save_output(employee_shifts_and_breaks_history_all_params, "employee_shifts_and_breaks_history_all_params")
    # else:
    #     logging.error("Failed to fetch employee_shifts_and_breaks_history with all params.")

    # --- Test get_employee_shifts_and_breaks_history (date parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # history_start_date_only_esabh = (datetime.utcnow() - timedelta(days=60)).isoformat() + "Z"
    # employee_shifts_and_breaks_history_date_params = get_employee_shifts_and_breaks_history(
    #     history_start_date=history_start_date_only_esabh
    # )
    # if employee_shifts_and_breaks_history_date_params:
    #     save_output(employee_shifts_and_breaks_history_date_params, "employee_shifts_and_breaks_history_date_params")
    # else:
    #     logging.error("Failed to fetch employee_shifts_and_breaks_history with date params.")

    # else:
    #     logging.error("Failed to fetch employee_shifts_and_breaks_history with date params.")

    # =================================================================
    # ================== WORK SHIFT DETAILS API CALLS =================
    # =================================================================

    # --- Test get_work_shift_details (all parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # last_updated_work_shift_details = (datetime.utcnow() - timedelta(days=30)).isoformat() + "Z"
    # work_shift_details_all_params = get_work_shift_details(
    #     page_size=10,
    #     start_date="2023-01-01", # CHANGE THIS
    #     end_date="2023-01-31", # CHANGE THIS
    #     creator="SOME_CREATOR_ID", # CHANGE THIS
    #     work_shift_keys=[1,2,3], # CHANGE THIS
    #     last_updated=last_updated_work_shift_details
    # )
    # if work_shift_details_all_params:
    #     save_output(work_shift_details_all_params, "work_shift_details_all_params")
    # else:
    #     logging.error("Failed to fetch work_shift_details with all params.")

    # --- Test get_work_shift_details (simple list) ---
    # Uncomment to run:
    # work_shift_details_list = get_work_shift_details()
    # if work_shift_details_list:
    #     save_output(work_shift_details_list, "work_shift_details_list")
    # else:
    #     logging.error("Failed to fetch work_shift_details list.")

    # else:
    #     logging.error("Failed to fetch work_shift_details list.")

    # =================================================================
    # ================ EMPLOYEE SHIFT DETAILS API CALLS ===============
    # =================================================================

    # --- Test get_employee_shift_details (all parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # last_updated_employee_shift_details = (datetime.utcnow() - timedelta(days=30)).isoformat() + "Z"
    # employee_shift_details_all_params = get_employee_shift_details(
    #     page_size=10,
    #     start_date="2023-01-01", # CHANGE THIS
    #     end_date="2023-01-31", # CHANGE THIS
    #     employee="SOME_EMPLOYEE_ID", # CHANGE THIS
    #     is_signed=True,
    #     last_updated=last_updated_employee_shift_details
    # )
    # if employee_shift_details_all_params:
    #     save_output(employee_shift_details_all_params, "employee_shift_details_all_params")
    # else:
    #     logging.error("Failed to fetch employee_shift_details with all params.")

    # --- Test get_employee_shift_details (simple list) ---
    # Uncomment to run:
    # employee_shift_details_list = get_employee_shift_details()
    # if employee_shift_details_list:
    #     save_output(employee_shift_details_list, "employee_shift_details_list")
    # else:
    #     logging.error("Failed to fetch employee_shift_details list.")

    # else:
    #     logging.error("Failed to fetch employee_shift_details list.")

    # =================================================================
    # =================== WORKFLOW ENTRIES API CALLS ==================
    # =================================================================

    # --- Test get_workflow_entries (all parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # last_updated_workflow_entries = (datetime.utcnow() - timedelta(days=30)).isoformat() + "Z"
    # workflow_entries_all_params = get_workflow_entries(
    #     page_size=10,
    #     job_number="SOME_JOB_NUMBER", # CHANGE THIS
    #     created_start_date="2023-01-01", # CHANGE THIS
    #     created_end_date="2023-01-31", # CHANGE THIS
    #     schema_id=123, # CHANGE THIS
    #     schema_name="SOME_SCHEMA_NAME", # CHANGE THIS
    #     variants="SOME_VARIANTS", # CHANGE THIS
    #     last_updated=last_updated_workflow_entries,
    #     status="SOME_STATUS", # CHANGE THIS
    #     include_deleted=False,
    #     is_active=True,
    #     expiration=30 # CHANGE THIS
    # )
    # if workflow_entries_all_params:
    #     save_output(workflow_entries_all_params, "workflow_entries_all_params")
    # else:
    #     logging.error("Failed to fetch workflow_entries with all params.")

    # --- Test get_workflow_entries (simple list) ---
    # Uncomment to run:
    # workflow_entries_list = get_workflow_entries()
    # if workflow_entries_list:
    #     save_output(workflow_entries_list, "workflow_entries_list")
    # else:
    #     logging.error("Failed to fetch workflow_entries list.")

    # else:
    #     logging.error("Failed to fetch workflow_entries list.")

    # =================================================================
    # =============== WORKFLOW ENTRIES HISTORY API CALLS ==============
    # =================================================================

    # --- Test get_workflow_entries_history (all parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # history_start_date_we = (datetime.utcnow() - timedelta(days=90)).isoformat() + "Z"
    # history_end_date_we = datetime.utcnow().isoformat() + "Z"
    # workflow_entries_history_all_params = get_workflow_entries_history(
    #     page_size=10,
    #     ids=[123, 456],  # CHANGE THIS
    #     history_start_date=history_start_date_we,
    #     history_end_date=history_end_date_we,
    #     history_type="UPDATED"  # CHANGE THIS (e.g., "CREATED", "UPDATED", "DELETED")
    # )
    # if workflow_entries_history_all_params:
    #     save_output(workflow_entries_history_all_params, "workflow_entries_history_all_params")
    # else:
    #     logging.error("Failed to fetch workflow_entries_history with all params.")

    # --- Test get_workflow_entries_history (date parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # history_start_date_only_we = (datetime.utcnow() - timedelta(days=60)).isoformat() + "Z"
    # workflow_entries_history_date_params = get_workflow_entries_history(
    #     history_start_date=history_start_date_only_we
    # )
    # if workflow_entries_history_date_params:
    #     save_output(workflow_entries_history_date_params, "workflow_entries_history_date_params")
    # else:
    #     logging.error("Failed to fetch workflow_entries_history with date params.")

    # else:
    #     logging.error("Failed to fetch workflow_entries_history with date params.")

    # =================================================================
    # =============== LOCKED TIME PERIODS API CALLS ===================
    # =================================================================

    # --- Test get_locked_time_periods (all parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # locked_time_periods_all_params = get_locked_time_periods(
    #     page_size=10
    # )
    # if locked_time_periods_all_params:
    #     save_output(locked_time_periods_all_params, "locked_time_periods_all_params")
    # else:
    #     logging.error("Failed to fetch locked_time_periods with all params.")

    # --- Test get_locked_time_periods (simple list) ---
    # Uncomment to run:
    # locked_time_periods_list = get_locked_time_periods()
    # if locked_time_periods_list:
    #     save_output(locked_time_periods_list, "locked_time_periods_list")
    # else:
    #     logging.error("Failed to fetch locked_time_periods list.")

    # else:
    #     logging.error("Failed to fetch locked_time_periods list.")

    # =================================================================
    # ======================= NOTES API CALLS =========================
    # =================================================================

    # --- Test get_notes (all parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # last_updated_notes = (datetime.utcnow() - timedelta(days=30)).isoformat() + "Z"
    # notes_all_params = get_notes(
    #     page_size=10,
    #     job_number="SOME_JOB_NUMBER", # CHANGE THIS
    #     start_date="2023-01-01", # CHANGE THIS
    #     end_date="2023-01-31", # CHANGE THIS
    #     last_updated=last_updated_notes
    # )
    # if notes_all_params:
    #     save_output(notes_all_params, "notes_all_params")
    # else:
    #     logging.error("Failed to fetch notes with all params.")

    # --- Test get_notes (simple list) ---
    # Uncomment to run:
    # notes_list = get_notes()
    # if notes_list:
    #     save_output(notes_list, "notes_list")
    # else:
    #     logging.error("Failed to fetch notes list.")

    # else:
    #     logging.error("Failed to fetch notes list.")

    # =================================================================
    # ==================== QUANTITY ENTRIES API CALLS =================
    # =================================================================

    # --- Test get_quantity_entries (all parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # last_updated_quantity_entries = (datetime.utcnow() - timedelta(days=30)).isoformat() + "Z"
    # quantity_entries_all_params = get_quantity_entries(
    #     page_size=10,
    #     job_number="SOME_JOB_NUMBER", # CHANGE THIS
    #     start_date="2023-01-01", # CHANGE THIS
    #     end_date="2023-01-31", # CHANGE THIS
    #     last_updated=last_updated_quantity_entries,
    #     foreman="SOME_FOREMAN_ID" # CHANGE THIS
    # )
    # if quantity_entries_all_params:
    #     save_output(quantity_entries_all_params, "quantity_entries_all_params")
    # else:
    #     logging.error("Failed to fetch quantity_entries with all params.")

    # --- Test get_quantity_entries (simple list) ---
    # Uncomment to run:
    # quantity_entries_list = get_quantity_entries()
    # if quantity_entries_list:
    #     save_output(quantity_entries_list, "quantity_entries_list")
    # else:
    #     logging.error("Failed to fetch quantity_entries list.")

    # else:
    #     logging.error("Failed to fetch quantity_entries list.")

    # =================================================================
    # ===================== EMAIL ALERTS API CALLS ====================
    # =================================================================

    # --- Test get_email_alerts (all parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # email_alerts_all_params = get_email_alerts(
    #     page_size=10,
    #     job_number="SOME_JOB_NUMBER", # CHANGE THIS
    #     company_supplied_id="SOME_COMPANY_SUPPLIED_ID", # CHANGE THIS
    # )
    # if email_alerts_all_params:
    #     save_output(email_alerts_all_params, "email_alerts_all_params")
    # else:
    #     logging.error("Failed to fetch email_alerts with all params.")

    # --- Test get_email_alerts (simple list) ---
    # Uncomment to run:
    # email_alerts_list = get_email_alerts()
    # if email_alerts_list:
    #     save_output(email_alerts_list, "email_alerts_list")
    # else:
    #     logging.error("Failed to fetch email_alerts list.")

    # else:
    #     logging.error("Failed to fetch email_alerts list.")

    # =================================================================
    # ================== START STOP TYPES API CALLS ===================
    # =================================================================

    # --- Test get_start_stop_types (all parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # start_stop_types_all_params = get_start_stop_types(
    #     page_size=10
    # )
    # if start_stop_types_all_params:
    #     save_output(start_stop_types_all_params, "start_stop_types_all_params")
    # else:
    #     logging.error("Failed to fetch start_stop_types with all params.")

    # --- Test get_start_stop_types (simple list) ---
    # Uncomment to run:
    # start_stop_types_list = get_start_stop_types()
    # if start_stop_types_list:
    #     save_output(start_stop_types_list, "start_stop_types_list")
    # else:
    #     logging.error("Failed to fetch start_stop_types list.")

if __name__ == "__main__":
    run_tests()