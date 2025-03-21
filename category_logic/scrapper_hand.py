import google.generativeai as genai


genai.configure(api_key = 'AIzaSyCJhwbGTw10OIe7Lyo1VMSVZu7ts13iHro')
model = genai.GenerativeModel('gemini-1.5-flash')

class logic_scrap:
    def respond(self, requirement):
        base_prompt = f'''extract the 'first_name', 'last_name', and "domain' from the prompt. 
        no need to mention or utput anything else.
        the prompt is : {requirement}
        '''
        try:
            response = model.generate_content(base_prompt)
            response_txt = response.text
            try:
                parts = response_txt.split('\n')
                result = {}
                for part in parts:
                    if ':' in part:
                        key, value = part.split(':', 1)
                        result[key.strip()] = value.strip()
                return result
            except:
                return response_txt
        except Exception as e:
            return f"An error occurred: {e}"
        
    
