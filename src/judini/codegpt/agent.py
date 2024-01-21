import requests

base_url = "https://api-beta.codegpt.co/api/v1/"

class Agent:
    def __init__(self, api_key):
        self.api_key = api_key


    def getAll(self):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        url = f"{base_url}/agent"

        try:
            response = requests.get(url, headers=headers)
            if response.status_code != 200:
                error_message = f"API Response: {response.status_code} {response.reason}"
                raise Exception(error_message)
            else:
                return response.json()

        except Exception as e:
            print(f"An error occurred: {e}")
    
    def getAgentById(self,agent_id):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        url = f"{base_url}/agent/{agent_id}"

        try:
            response = requests.get(url, headers=headers)
            if response.status_code != 200:
                error_message = f"API CODEGPT Response: {response.status_code} {response.reason}"
                raise Exception(error_message)
            else:
                return response.json()

        except Exception as e:
            print(f"An error occurred: {e}")

    def update(self,agent_id, data):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        url = f"{base_url}/agent/{agent_id}"
        try:
            response = requests.patch(url, json=data, headers=headers)
            if response.status_code != 200:
                error_message = f"API Response was: {response.status_code} {response.reason}"
                raise Exception(error_message)
            else:
                return response.json()

        except Exception as e:
            print(f"An error occurred: {e}")    