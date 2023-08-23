import pytest
from judini.agent import Agent
import os
from dotenv import load_dotenv
load_dotenv()

def test_completion():
    #Judini
    judini_api_key= os.getenv("JUDINI_API_KEY")
    judini_agent_id= os.getenv("JUDINI_AGENT_ID")

    agent_instance = Agent(api_key=judini_api_key, agent_id=judini_agent_id)

    prompt = 'Quien es el presidente de Chile?'
    response = agent_instance.completion(prompt, stream=False)

    print(f"Response: {response}")

    assert isinstance(response, str) and len(response) > 0
