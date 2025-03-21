from Gemma.prompt_handler import program_response
from Gemma.generator import writer
from Gemma.DB_logic import DB_logic
from call_api.hunter_api import Scrapper
from call_api.db_scan import DataSheetChecker
from catgeory_logic.scrapper_hand import logic_scrap

program_response_obj = program_response()
writer_obj = writer()
DBMS_obj = DB_logic()
handler_obj = logic_scrap()
scrapper_obj = Scrapper()
data_checker = DataSheetChecker("data.xlsx", "Sheet")

file_path = "data.xlsx"
sheet = 'Sheet'
class AppLogic:
    def process_prompt(self, user_input):
        """Processes the user input and extracts categories."""
        response_text = program_response_obj.respond(user_input)
        return response_text['category']

    def execute(self, user_input):
        """Handles the logic for Scrapper & Generation categories."""
        extracted_categories = self.process_prompt(user_input)
        db_data = {}  # Ensure db_data is always defined
        response_text = ""

        if "Scrapper" in extracted_categories:
            scrap_dict = handler_obj.respond(user_input)
            checker_dict = {'name': scrap_dict['first_name'] + scrap_dict['last_name']}
            existing_entry = data_checker.check_entry(checker_dict)

            if existing_entry:
                db_data = {
                    "email": existing_entry.get('email'),
                    "name": existing_entry.get('name'),
                    "company": existing_entry.get('company')
                }
                response_text = f"Entry found in datasheet:\n  mail:{db_data['email']}\n name:{db_data['name']}\n company:{db_data['company']}"

            else:
                response_text = "Entry not found, proceeding with scraping.\n"
                scrapper_obj = Scrapper(**scrap_dict)
                scrapper_out = scrapper_obj.find_email()

                db_data = {
                    "email": scrapper_out.get('email'),
                    "name": scrapper_out.get('name'),
                    "company": scrapper_out.get('company')
                }
                response_text = f"Scraped Data: \n  mail:{db_data['email']}\n name:{db_data['name']}\n company:{db_data['company']}"

                data_checker.add_entry(db_data)

        if "Generation" in extracted_categories:
            generation_output = writer_obj.respond(user_input + str(db_data))
            response_text = f"Generated Output: {generation_output}"

        return response_text  




