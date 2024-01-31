import json
import requests
from typing import List, Dict, Literal

base_url = "https://api-beta.codegpt.co/api/v1"

class Completion:
    def __init__(self, api_key):
        self.api_key = api_key

    def create(self, agent_id: str, messages: List[Dict[str, str]], 
               stream: bool = False, format: Literal['json', 'text'] = 'text') -> str:
        headers = {
            "Content-Type": "application/json",
            "media_type": "text/event-stream",
            "Authorization": f"Bearer {self.api_key}"
        }

        payload = json.dumps({
            "agentId": agent_id,
            "messages": messages,
            "stream": stream,
            "format": "json" # By default always json
        })

        response = requests.post(f"{base_url}/chat/completions", headers=headers,
                                  data=payload, stream=stream)

        if stream:
            return self._handle_stream(response, format)
        else:
            return self._handle_non_stream(response, format)
        
    def _handle_stream(self, response: requests.Response,
                       format: Literal['json', 'text']) -> List[str]:
        try:
            for chunk in response.iter_lines():
                if chunk:
                    chunk_str = chunk.decode("utf-8")
                    data_array = chunk_str.replace('\n','').split('data: ')[1:]
                    for jd_str in data_array:
                        if jd_str == '[DONE]':
                            break
                        json_data = json.loads(jd_str)
                        if format == 'json':
                            yield json_data
                        elif format == 'text':
                            for item in json_data['choices']:
                                yield item['delta']['content']
        except Exception as e:
            print(f"Error occurred: {e}", jd_str)
        finally:
            response.close()

    def _handle_non_stream(self, response: requests.Response,
                           format: Literal['json', 'text']) -> str:
        try:
            json_data = response.json()
            if format == 'json':
                return json_data
            elif format == 'text':
                return json_data['choices'][0]['message']['content']
        except Exception as e:
            print(f"Error occurred: {e}")
        finally:
            response.close()
        