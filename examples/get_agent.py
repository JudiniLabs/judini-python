# Import necessary modules and libraries
import os
import asyncio
from judini.codegpt.agent import Agent
from dotenv import load_dotenv  # For loading environment variables from a .env file

# Load environment variables from a .env file if available
load_dotenv()


# Define an asynchronous function to retrieve information about a CodeGPT agent

async def info_agent():
    # Retrieve the CodeGPT API key from environment variables
    CODEGPT_API_KEY = os.getenv("CODEGPT_API_KEY")

    # Retrieve the CodeGPT agent ID from environment variables (or you can provide it directly)
    # You can also specify the agent ID directly
    CODEGPT_AGENT_ID = os.getenv("CODEGPT_AGENT_ID")

    # Create an instance of the CodeGPT agent using the API key and agent ID
    # If you want to list information for all agents, use the following line without specifying the agent ID
    # agent_instance = Agent(api_key=CODEGPT_API_KEY)

    # If you want to list information for a specific agent, specify the agent ID
    agent_instance = Agent(api_key=CODEGPT_API_KEY, agent_id=CODEGPT_AGENT_ID)

    # Use the agent instance to retrieve information about the agent
    response = await agent_instance.get()

    # Print the response containing information about the agent
    print(response)

# Entry point of the script
if __name__ == "__main__":
    # Run the info_agent function to retrieve agent information using asyncio
    asyncio.run(info_agent())
