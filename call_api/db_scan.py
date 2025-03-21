import openpyxl

class DataSheetChecker:
    def __init__(self, file_path, sheet_name):
        """Initializes the DataSheetChecker with the given Excel file and sheet name."""
        self.file_path = file_path
        self.sheet_name = sheet_name
        self.wb = openpyxl.load_workbook(file_path)
        self.sheet = self.wb[sheet_name]

        # Extract column headers from the first row
        self.headers = [cell.value for cell in self.sheet[1]]  

    def check_entry(self, scrap_dict):
        """Checks if the requested person's details exist in the Excel sheet."""
        
        # Extract details from scrap_dict
        name = scrap_dict.get("name", "").strip().lower()
        domain = scrap_dict.get("domain", "").strip().lower()

        if not all([name, domain]):  # Ensure required fields exist
            return None  # Invalid input, cannot check

        # Iterate through the sheet to find a matching entry
        for row in self.sheet.iter_rows(min_row=2, values_only=True):  # Skip header
            existing_name, existing_domain, existing_email = (row + (None,) * 3)[:3]  

            # Ensure values are strings for safe comparison
            existing_name = (existing_name or "").strip().lower()
            existing_domain = (existing_domain or "").strip().lower()
            existing_email = existing_email or None  # Keep None for missing emails

            # Check if the person exists in the database
            if existing_name == name and existing_domain == domain:
                return {
                    "name": existing_name,
                    "domain": existing_domain,
                    "email": existing_email
                }

        return None  # Entry not found

    def add_entry(self, new_data):
        """
        Adds a new entry to the Excel sheet if it does not exist.
        
        Parameters:
            new_data (dict): Dictionary containing keys that match the column names.
        """
        # Ensure all required columns exist in new_data
        row_data = [new_data.get(col, "") for col in self.headers]  

        # Append new row to the sheet
        self.sheet.append(row_data)
        self.wb.save(self.file_path)  # Save changes
        print("New entry added to the database.")

    def close(self):
        """Closes the workbook."""
        self.wb.close()
