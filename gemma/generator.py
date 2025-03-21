import google.generativeai as genai


genai.configure(api_key = 'AIzaSyCJhwbGTw10OIe7Lyo1VMSVZu7ts13iHro')
model = genai.GenerativeModel('gemini-1.5-flash')

class writer:
    def respond(self, requirement):
        base_prompt = f'''write for: {requirement}
        '''
        response = model.generate_content(base_prompt)
        response_txt = response.text
        return response_txt
    

