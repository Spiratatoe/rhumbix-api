# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python CLI tool for interacting with the Rhumbix API. It fetches data from API endpoints and saves responses as JSON and CSV files for testing and validation purposes.

## Commands

```bash
# Set up virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Unix

# Install dependencies
pip install -r requirements.txt

# Run API tests
python main.py
```

## Configuration

Create a `.env` file in the root directory:
```
RHUMBIX_API_KEY="your_api_key_here"
RHUMBIX_BASE_URL="https://api.rhumbix.com/v1"
```

## Architecture

- `main.py` - Entry point with test runner. Contains commented-out test blocks for each API endpoint. Uncomment specific blocks to run tests. Output saves to `output/` directory.
- `src/config.py` - Loads API credentials from environment variables
- `src/utils.py` - Contains `get_all_paginated_results()` helper for handling paginated API responses
- `src/<resource>/api.py` - Each Rhumbix API resource has its own module (e.g., `employees`, `projects`, `cost_codes`)

## Development Conventions

- Each API resource should have its own module in `src/<resource>/api.py`
- All paginated API calls must use `get_all_paginated_results()` from `src/utils.py`
- API functions should accept optional filter parameters and return `List[Dict]`
- Parameters with `None` values are stripped before making requests
- To test a new endpoint, add a test block to `run_tests()` in `main.py`
