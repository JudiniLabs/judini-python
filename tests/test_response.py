from judini.agent import Agent
from dotenv import load_dotenv
import os
load_dotenv()


judini_api_key= os.getenv("JUDINI_API_KEY")
judini_agent_id= os.getenv("JUDINI_AGENT_ID")

agent_instance = Agent(api_key=judini_api_key, agent_id=judini_agent_id)

prompt = 'Quien es el presidente de Chile?'
response = agent_instance.completion(prompt, stream=True)

print(response)

