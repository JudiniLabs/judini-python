import asyncio
import os
import pytest
from .agent import Agent

@pytest.mark.asyncio
async def test_agent():
    # Cargar las credenciales del agente
    api_key = os.getenv('CODEGPT_API_KEY')
    agent_id = os.getenv('CODEGPT_AGENT_ID')

    # Crear una instancia del agente
    agent = Agent(api_key, agent_id)

    # Definir el mensaje de prueba
    prompt = "Can you help me?"

    # Prueba con stream=False
    response = await agent.completion(prompt, stream=False)
    print(f"Response with stream=False: {response}")

    # Prueba con stream=True
    response = await agent.completion(prompt, stream=True)
    print(f"Response with stream=True: {response}")

if __name__ == "__main__":
    asyncio.run(test_agent())
