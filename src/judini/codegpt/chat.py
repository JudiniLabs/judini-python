import requests

base_url = "https://api-beta.codegpt.co/api/v1/"

class Completion:
    def __init__(self, api_key):
        self.api_key = api_key


    def create(self, agent_id, messages, stream=False):
            # Define los valores de headers, messages y la neueva URL
            headers = {
                "Content-Type": "application/json",
                "media_type": "text/event-stream",
                "Authorization": f"Bearer {self.api_key}"
            }

            json = {
                "agent": agent_id,
                "messages": messages,
                "stream": stream,
            }
           
            url = f"{base_url}/chat/completions"

            if stream is False:
                try:
                    response = requests.post(url, json=json, headers=headers)
                    if response.status_code != 200:
                        error_message = f"API Response was: {response.status_code} {response.reason}"
                        raise Exception(error_message)
                    

                    return response.json().split('data: ')[1]
                
                except Exception as e:
                    print(f"An error occurred: {e}")
            else:
                try:
                    response = requests.post(url, json=json, headers=headers)
                    if response.status_code != 200:
                        error_message = f"API Response was: {response.status_code} {response.reason}"
                        raise Exception(error_message)

                    return response.text.split('data: ')
                
                except Exception as e:
                    print(f"An error occurred: {e}")
