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