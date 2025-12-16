import logging
import os
from datetime import datetime, timedelta
import json
import pandas as pd

from src.company_groups.api import get_rhumbix_ou_list, get_company_groups_details
from src.absence_types.api import get_absence_types
from src.absences.api import get_absences
from src.budgets.api import get_budgets
from src.clock_entries.api import get_clock_in_clock_out_entries
from src.clock_timelines.api import get_clock_in_clock_out_timelines
from src.cohorts.api import get_cohorts
from src.companies.api import get_companies
from src.cost_codes.api import get_cost_codes
from src.employees.api import get_employees
from src.equipment.api import get_equipment
from src.field_folder_notes.api import get_field_folder_notes
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
    # ============ CLOCK IN/OUT ENTRIES API CALLS =====================
    # =================================================================

    # --- Test get_clock_in_clock_out_entries (all parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # start_time_clock_entries_all = (datetime.utcnow() - timedelta(days=15)).isoformat() + "Z"
    # end_time_clock_entries_all = datetime.utcnow().isoformat() + "Z"
    # last_updated_clock_entries_all = (datetime.utcnow() - timedelta(days=7)).isoformat() + "Z"
    # clock_entries_all_params = get_clock_in_clock_out_entries(
    #     page_size=5,
    #     last_updated=last_updated_clock_entries_all,
    #     worker=["WORKER_ID_1", "WORKER_ID_2"], # CHANGE THIS
    #     start_time=start_time_clock_entries_all,
    #     end_time=end_time_clock_entries_all,
    #     only_edited=True,
    #     entry_id=["ENTRY_ID_1", "ENTRY_ID_2"], # CHANGE THIS
    #     include_deleted=False
    # )
    # if clock_entries_all_params:
    #     save_output(clock_entries_all_params, "clock_entries_all_params")
    # else:
    #     logging.error("Failed to fetch clock entries with all params.")

    # --- Test get_clock_in_clock_out_entries (date parameters) ---
    # Uncomment to run (adjust parameters as needed):
    # start_time_clock_entries_date = (datetime.utcnow() - timedelta(days=60)).isoformat() + "Z"
    # end_time_clock_entries_date = (datetime.utcnow() - timedelta(days=30)).isoformat() + "Z"
    # clock_entries_date_params = get_clock_in_clock_out_entries(
    #     start_time=start_time_clock_entries_date,
    #     end_time=end_time_clock_entries_date
    # )
    # if clock_entries_date_params:
    #     save_output(clock_entries_date_params, "clock_entries_date_params")
    # else:
    #     logging.error("Failed to fetch clock entries with date params.")

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

if __name__ == "__main__":
    run_tests()