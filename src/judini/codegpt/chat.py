import requests


url_server = "https://api.codegpt.co"
url_documentation = "https://developers.codegpt.co"

class Completion:
    def __init__(self, api_key):
        self.api_key = api_key


    def create(self, agent_id, prompt, stream=False, as_openai_response = False):
            # Define los valores de headers, messages y la neueva URL
            headers = {
                "Content-Type": "application/json",
                "media_type": "text/event-stream",
                "Authorization": f"Bearer {self.api_key}"
            }

            try:
                prompt[0]
            except:
                prompt = [prompt]

            messages = {
                "agent": agent_id,
                "messages": prompt,
                "stream": stream,
            }
            if as_openai_response is False:
                url = f"{url_server}/v1/completion"
            else:
                url = f"{url_server}/v1/chat/completions"

            if stream is False:
                try:
                    response = requests.post(url, json=messages, headers=headers)
                    if response.status_code != 200:
                        error_message = f"API Response was: {response.status_code} {response.reason} {url_documentation}"
                        raise Exception(error_message)
                    

                    return response.json().split('data: ')[1]
                
                except Exception as e:
                    print(f"An error occurred: {e}")
            else:
                try:
                    response = requests.post(url, json=messages, headers=headers)
                    if response.status_code != 200:
                        error_message = f"API Response was: {response.status_code} {response.reason} {url_documentation}"
                        raise Exception(error_message)

                    return response.text.split('data: ')
                
                except Exception as e:
                    print(f"An error occurred: {e}")
