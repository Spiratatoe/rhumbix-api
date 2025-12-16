import logging
from datetime import datetime, timedelta
import json
import os
import pandas as pd

from src.company_groups.api import get_rhumbix_ou_list, get_company_groups_details
from src.absence_types.api import get_absence_types
from src.config import API_KEY, BASE_URL

# Configure logging
logging.basicConfig(level=logging.INFO)

OUTPUT_DIR = "output"


def save_output(data, filename_prefix):
    """
    Saves the given data to JSON and CSV files.
    """
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    json_path = os.path.join(OUTPUT_DIR, f"{filename_prefix}.json")
    csv_path = os.path.join(OUTPUT_DIR, f"{filename_prefix}.csv")

    # Save as JSON
    with open(json_path, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Successfully saved JSON output to {json_path}")

    # Save as CSV
    try:
        df = pd.json_normalize(data)
        df.to_csv(csv_path, index=False)
        print(f"Successfully saved CSV output to {csv_path}")
    except Exception as e:
        print(f"Could not save CSV file: {e}")


def pretty_print(data):
    """Helper function to print data in a readable format."""
    print(json.dumps(data, indent=2))


def main():
    """
    Main function to test Rhumbix API calls.

    This file serves as a testbed for all the API calls defined in the src modules.
    To test a specific function, uncomment the corresponding code block below.
    The output of each run will be saved in the 'output' directory.
    """
    if not API_KEY or "your_api_key_here" in API_KEY or not BASE_URL:
        logging.error("API_KEY is not set. Please check your .env file.")
        logging.error(
            "Make sure you have a .env file in the root directory with RHUMBIX_API_KEY set."
        )
        logging.error("Refer to .env.example for the correct format.")
        return

    print("Rhumbix API Test Runner")
    print("Uncomment the function you want to test in main.py")
    print("="*50)

    # =================================================================
    # =============== COMPANY GROUPS API CALLS ========================
    # =================================================================

    # --- Test 1: Get a simple list of all Organizational Units (OUs) ---
    # Uncomment the block below to test 'get_rhumbix_ou_list'
    # -----------------------------------------------------------------
    # print("\n--- Testing: get_rhumbix_ou_list() ---")
    # ou_list = get_rhumbix_ou_list()
    # if ou_list:
    #     print("Successfully fetched OU list.")
    #     save_output(ou_list, "ou_list")
    # else:
    #     print("Failed to fetch OU list or no OUs found.")
    # print("-" * 50)

    # --- Test 2: Get a detailed list of all Company Groups ---
    # Uncomment the block below to test 'get_company_groups_details'
    # -------------------------------------------------------------
    # print("\n--- Testing: get_company_groups_details() ---")
    # detailed_groups = get_company_groups_details()
    # if detailed_groups:
    #     print("Successfully fetched detailed company groups.")
    #     save_output(detailed_groups, "company_groups_detailed")
    # else:
    #     print("Failed to fetch detailed company groups or none found.")
    # print("-" * 50)

    # --- Test 3: Get Company Groups with parameters ---
    # Example: Get groups updated in the last 7 days with a page size of 5
    # Uncomment the block below to test 'get_company_groups_details' with params
    # --------------------------------------------------------------------
    # print("\n--- Testing: get_company_groups_details() with parameters ---")
    # seven_days_ago = (datetime.utcnow() - timedelta(days=7)).isoformat() + "Z"
    # page_size = 5
    # print(f"Fetching groups updated since {seven_days_ago} with page size {page_size}...")
    # recent_groups = get_company_groups_details(last_updated=seven_days_ago, page_size=page_size)
    # if recent_groups:
    #     print("Successfully fetched recent company groups.")
    #     save_output(recent_groups, "company_groups_recent")
    # elif recent_groups == []:
    #      print("No company groups match the specified criteria.")
    # else:
    #     print("Failed to fetch recent company groups.")
    # print("-" * 50)


    # =================================================================
    # ================ ABSENCE TYPES API CALLS ========================
    # =================================================================

    # --- Test 4: Get a list of all Absence Types ---
    # Uncomment the block below to test 'get_absence_types'
    # -----------------------------------------------------------------
    # print("\n--- Testing: get_absence_types() ---")
    # absence_types = get_absence_types()
    # if absence_types:
    #     print("Successfully fetched absence types.")
    #     save_output(absence_types, "absence_types")
    # else:
    #     print("Failed to fetch absence types or none found.")
    # print("-" * 50)


if __name__ == "__main__":
    main()
