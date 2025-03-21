   
import google.generativeai as genai
import json

genai.configure(api_key='AIzaSyCJhwbGTw10OIe7Lyo1VMSVZu7ts13iHro')
model = genai.GenerativeModel('gemini-1.5-flash')



class program_response:
    def respond(self, usr_inp):
        base_prompt = f"""
        You are a prompt handler. Your task is NOT to answer the user's query but to analyze it and return a structured JSON response.
        
        Return ONLY a valid JSON object in this format:

        {{
            "prompt_requirement": "<Briefly describe what the user is asking>",
            "category": ["<One or more categories from: 'Database', 'Scrapper', 'Generation'>"],
            "action": ["<The specific verb(s) the user wants, e.g., 'update', 'scrape', 'generate'>"],
            "scrapper_requirement": {{
                "task": "<Describe the scraping task>",
                "first_name": "<Extracted first name if mentioned, otherwise null>",
                "last_name": "<Extracted last name if mentioned, otherwise null>",
                "domain": "<Extracted domain if mentioned, otherwise null>"
            }}
        }}

        DO NOT return any extra text or formatting. Output raw JSON without code blocks.

        User input: {usr_inp}
        """
        try:
            response = model.generate_content(base_prompt)
            response_txt = response.text.strip()

            # Fix: Remove Markdown-style code blocks if they exist
            if response_txt.startswith("```json"):
                response_txt = response_txt[7:]  # Remove the opening ```json
            if response_txt.endswith("```"):
                response_txt = response_txt[:-3]  # Remove the closing ```

            # Attempt to parse JSON
            try:
                return json.loads(response_txt)
            except json.JSONDecodeError:
                return {"error": "Invalid JSON response from AI", "raw_response": response_txt}

        except Exception as e:
            return {"error": f"An error occurred: {e}"}