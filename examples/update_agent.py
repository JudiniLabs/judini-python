# Import necessary modules and libraries
import os
import asyncio
from judini.codegpt.agent import Agent
from dotenv import load_dotenv  # For loading environment variables from a .env file

# Load environment variables from a .env file if available
load_dotenv()


# Define an asynchronous function to update information about a CodeGPT agent

async def update_agent():
    # Retrieve the CodeGPT API key from environment variables
    CODEGPT_API_KEY = os.getenv("CODEGPT_API_KEY")

    # Retrieve the CodeGPT agent ID from environment variables (or you can provide it directly)
    # You can also specify the agent ID directly
    CODEGPT_AGENT_ID = os.getenv("CODEGPT_AGENT_ID")

    # Create an instance of the CodeGPT agent using the API key and agent ID
    agent_instance = Agent(api_key=CODEGPT_API_KEY, agent_id=CODEGPT_AGENT_ID)

    # Define the data to update the agent information
    data = {
        "name": "DevBot",  # Update the agent's name
        "prompt": "New Prompt",  # Update the agent's prompt
    }

    # Use the agent instance to update the agent's information with the provided data
    response = await agent_instance.update(data)

    # Print the response to confirm the update
    print(response)

# Entry point of the script
if __name__ == "__main__":
    # Run the update_agent function to update agent information using asyncio
    asyncio.run(update_agent())
