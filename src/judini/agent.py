# Agent
import requests
import json

class Agent:
    def __init__(self, api_key, agent_id):
        self.api_key = api_key
        self.agent_id = agent_id

    def set_api_key(self, api_key):
        self.api_key = api_key

    def set_agent_id(self, agent_id):
        self.agent_id = agent_id

    def completion(self, prompt, stream=False):
        # Headers
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        # Endpoint
        url = 'https://playground.judini.ai/api/v1/agent/'+ self.agent_id
        data = {
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }
        response = requests.post(url, json=data, headers=headers)
        tokens = ''
        error = ''
        if(stream == False):
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    raw_data = chunk.decode('utf-8').replace("data: ", '')
                    if raw_data != "":
                        lines = raw_data.strip().splitlines()
                        for line in lines:
                            line = line.strip()
                            if line and line != "[DONE]":
                                try:
                                    json_object = json.loads(line)
                                    result = json_object['data']
                                    result = result.replace("\n", "")
                                    tokens += result
                                except json.JSONDecodeError:
                                    error = line
                                    #print(f'Error al decodificar el objeto JSON en la línea: {line}')    
        else:
            return response
        
        return tokens