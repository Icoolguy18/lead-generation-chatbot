import google.generativeai as genai
import openpyxl


genai.configure(api_key = 'AIzaSyCJhwbGTw10OIe7Lyo1VMSVZu7ts13iHro')
model = genai.GenerativeModel('gemini-1.5-flash')




class DB_logic:
    def respond(self, requirement):
        base_prompt = f'''You are a database assistant that manages an Excel-based DBMS.
        Your task is to write ONLY the openpyxl code syntax to carry out the given task in the Excel sheet.
        Users will input queries regarding the data.
        You MUST identify the required details and write ONLY the openpyxl code syntax.
        Use ONLY the 'openpyxl' library.
        You MUST break down the request and understand what action is required.
        As of now, ignore any ambiguity regarding the data.
        Your ONLY output MUST be the openpyxl code syntax.
        DO NOT include any explanations, comments, or other text.
        DO NOT define any functions.
        if the column names are set already no need to update them. 
        if the user prompt is a dict, based on the keys sort and append the data in the correct place
        User Input: {requirement}
        Output:
        wb = load_workbook('data.xlsx')
        ws = wb['Sheet']
        # ... (rest of the code) ...
        '''
        try:
            response = model.generate_content(base_prompt)
            response_txt = response.text.strip()

            # Fix: Remove Markdown-style code blocks if they exist
            if response_txt.startswith("```python"):
                response_txt = response_txt[9:]  # Remove the opening ```json
            if response_txt.endswith("```"):
                response_txt = response_txt[:-3]  # Remove the closing ```
            return response_txt
        except Exception as e:
            return {"error": f"An error occurred: {e}"}


