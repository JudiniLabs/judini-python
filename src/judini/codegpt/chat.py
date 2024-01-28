import http
import json

base_url = "https://api-beta.codegpt.co/api/v1"

class Completion:
    def __init__(self, api_key):
        self.api_key = api_key


    def create(self, agent_id, messages, stream=False):
            headers = {
                "Content-Type": "application/json",
                "media_type": "text/event-stream",
                "Authorization": f"Bearer {self.api_key}"
            }

            payload = json.dumps({
                "agentId": agent_id,
                "messages": messages
            })

            conn = http.client.HTTPSConnection("api-beta.codegpt.co")
            url = "/api/v1/chat/completions"

            conn.request("POST", url, body=payload, headers=headers)
            res = conn.getresponse()
            try:
                data = res.read()
            except Exception as e:
                print(f"An error occurred: {e.__class__.__name__}")
                print(f"Error details: {str(e)}")

            content_data = ""
            if stream is False:
                data.decode("utf-8").replace('\n','').split('data: ')[1:]
                for jd_str in data:
                    if jd_str:
                        try:
                            # data: {}
                            json_data = json.loads(jd_str)
                            for item in json_data['choices']:
                                content_data += item['delta']['content']
                        except:
                            # data: [DONE]
                            pass

                return content_data
            else:
                try:
                    return data.decode("utf-8").replace('\n','').split('data: ')[1:]
                except Exception as e:
                    print(f"An error occurred: {e.__class__.__name__}")
                    print(f"Error details: {str(e)}")
