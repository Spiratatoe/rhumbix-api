# Project Overview

This project is a Python-based command-line tool for interacting with the Rhumbix API. Its main purpose is to fetch data from various API endpoints, save the responses as both JSON and CSV files, and allow for testing and validation of the API data.

The project is structured as a client library, with a clear separation of concerns:
- `main.py`: The main entry point for executing predefined API test calls.
- `src/`: Contains the core application logic.
  - `config.py`: Manages API credentials and configuration using environment variables.
  - `utils.py`: Provides a helper function to handle paginated API responses.
  - Each subdirectory in `src/` (e.g., `employees`, `projects`) corresponds to a specific Rhumbix API resource and contains the logic for fetching data from that resource.

The main dependencies are `requests` for making HTTP calls, `pandas` for data manipulation and CSV export, and `python-dotenv` for managing environment variables.

# Building and Running

To run this project, follow these steps:

1.  **Set up the environment:**
    Create a `.env` file in the root directory with the following content, replacing the placeholder values with your actual Rhumbix API credentials:
    ```
    RHUMBIX_API_KEY="your_api_key_here"
    RHUMBIX_BASE_URL="https://api.rhumbix.com/v1"
    ```

2.  **Install dependencies:**
    It is recommended to use a virtual environment.
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3.  **Run the application:**
    Open `main.py` and uncomment the specific API call you wish to test within the `run_tests()` function. Then, run the script:
    ```bash
    python main.py
    ```
    The output files (JSON and CSV) will be saved in the `output/` directory.

# Development Conventions

*   **Configuration:** All configuration, especially secrets like API keys, should be managed through the `.env` file and accessed via the `src/config.py` module.
*   **API Modules:** Each API resource should have its own module (e.g., `src/employees/api.py`). This module should contain a function that encapsulates the logic for fetching data from that specific API endpoint.
*   **Pagination:** All paginated API calls should use the `get_all_paginated_results` utility from `src/utils.py` to ensure consistent handling of pagination.
*   **Error Handling:** API call functions should include error handling to gracefully manage failed requests. The current convention is to log errors and return an empty list.
*   **Testing:** The `main.py` file serves as the primary tool for integration testing. To test an endpoint, add a new test block to the `run_tests` function.
