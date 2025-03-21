import requests

API_KEY = "31e9f9379662b34b1f44389235bd73c9e414e965"

class Scrapper:
    def __init__(self, domain=None, first_name=None, last_name=None):
        self.domain = domain
        self.first_name = first_name
        self.last_name = last_name

    def find_email(self):
        if not all([self.domain, self.first_name, self.last_name]):
            return {"error": "Missing required parameters"}
        
        url = f"https://api.hunter.io/v2/email-finder?domain={self.domain}&first_name={self.first_name}&last_name={self.last_name}&api_key={API_KEY}"
        response = requests.get(url)

        try:
            data = response.json()  # Ensure JSON parsing
        except ValueError:
            return {"error": "Invalid response from API", "response_text": response.text}

        # Debugging
        #print("API Response:", data)  

        # Ensure "data" exists in the response and is a dictionary
        if not isinstance(data, dict) or "data" not in data:
            return {"error": "Unexpected API response format", "response": data}

        extracted_data = {
            "email": data.get("data", {}).get("email"),
            "name": f"{data.get('data', {}).get('first_name', '')} {data.get('data', {}).get('last_name', '')}".strip().lower(),
            "company": data.get("data", {}).get("company")  # Directly get the string value
        }
        return extracted_data

# Example usage
