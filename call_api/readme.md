
# Database Management, Data Scanning, and Email Scraping Overview

This document provides an overview of the database management, data scanning, and email scraping functionalities of the chatbot application.

## 1. Database Management (`db_manager.py`)

The `db_manager.py` file defines the `DBMS` class, which manages an Excel-based database using `openpyxl`.

### Key Components:
- **`_initialize_database()`**: Creates an Excel file with a default sheet if it does not exist.
- **`_get_workbook()`**: Loads the Excel workbook.
- **`set_headers(headers)`**: Sets column headers if the sheet is empty.
- **`add_record(record)`**: Appends a new record to the sheet.
- **`fetch_records()`**: Retrieves all records as a list of tuples.
- **`update_record(search_column, search_value, update_column, new_value)`**: Updates a specific record in the sheet.
- **`sort_records(sort_column, ascending=True)`**: Sorts records based on a specified column.

## 2. Data Scanning (`db_scan.py`)

The `db_scan.py` file defines the `DataSheetChecker` class, which verifies and updates records in the Excel database.

### Key Components:
- **`check_entry(scrap_dict)`**:
  - Checks if an entry exists in the sheet.
  - Matches `name` and `domain` fields to determine existence.
  - Returns stored details if a match is found, otherwise returns `None`.
- **`add_entry(new_data)`**:
  - Appends a new record to the sheet if it does not already exist.
  - Saves the updated file.
- **`close()`**: Closes the workbook.

## 3. Email Scraping (`hunter_api.py`)

The `hunter_api.py` file defines the `Scrapper` class, which interacts with the Hunter.io API to find emails based on user-provided details.

### Key Components:
- **`Scrapper(domain, first_name, last_name)`**: Initializes the scraper with required attributes.
- **`find_email()`**:
  - Constructs an API request to Hunter.io.
  - Sends a request with the given `domain`, `first_name`, and `last_name`.
  - Parses the API response and extracts the email, name, and company.
  - Returns extracted details or an error message in case of issues.

## 4. Integration and Workflow
1. User queries for an email or checks if an entry exists in the database.
2. `DataSheetChecker` verifies if the requested details exist.
3. If not found, `Scrapper` fetches the email using the Hunter.io API.
4. New data is appended to the Excel sheet.
5. The final response is sent to the user.

## 5. Future Enhancements
- Improve error handling for API failures.
- Optimize database queries for faster lookups.
- Implement caching to reduce redundant API calls.

