import requests


url_server = "https://api.codegpt.co"
url_documentation = "https://developers.codegpt.co"


class Agent:
    def __init__(self, api_key):
        self.api_key = api_key


    def getAll(self):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        url = f"{url_server}/v1/agent"

        try:
            response = requests.get(url, headers=headers)
            if response.status_code != 200:
                error_message = f"API Response was: {response.status_code} {response.reason} {url_documentation}"
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

        url = f"{url_server}/v1/agent/{agent_id}" if agent_id else f"{url_server}/v1/agent"

        try:
            response = requests.get(url, headers=headers)
            if response.status_code != 200:
                error_message = f"API Response was: {response.status_code} {response.reason} {url_documentation}"
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
        url = f"{url_server}/v1/agent/{agent_id}"
        try:
            response = requests.patch(url, json=data, headers=headers)
            if response.status_code != 200:
                error_message = f"API Response was: {response.status_code} {response.reason} {url_documentation}"
                raise Exception(error_message)
            else:
                return response.json()

        except Exception as e:
            print(f"An error occurred: {e}")



    def linkDocument(self,agent_id, documentId):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        url = f"{url_server}/v1/agent/{agent_id}"
        try:
            old_documentId = self.getAgentById(agent_id)["documentId"]
            old_documentId.append(documentId)
            data = {
                "documentId":old_documentId
            }

            response = requests.patch(url, json=data, headers=headers)
            if response.status_code != 200: 
                error_message = f"API Response: Error {response.status_code} {response.json()['detail']} {url_documentation}"
                raise Exception(error_message)
            else:
                return response.json()

        except Exception as e:
            print(f"An error occurred: {e}")

    
    def unlinkDocument(self,agent_id, documentId):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        url = f"{url_server}/v1/agent/{agent_id}"
        try:
            old_documentId = self.getAgentById(agent_id)["documentId"]
            old_documentId.remove(documentId) 

            if old_documentId is None:
                old_documentId = []
            
            data = {
                "documentId":old_documentId
            }
            response = requests.patch(url, json=data, headers=headers)
            if response.status_code != 200: 
                error_message = f"API Response was: {response.status_code} {response.reason} {url_documentation}"
                raise Exception(error_message)
            else:
                return response.json()

        except Exception as e:
            print(f"An error occurred: {e}")



    