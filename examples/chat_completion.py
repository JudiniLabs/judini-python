# Import necessary modules and libraries
import os
import asyncio
from judini.codegpt.agent import Agent
from dotenv import load_dotenv  # For loading environment variables from a .env file

# Load environment variables from a .env file if available
load_dotenv()


# Define an asynchronous function to demonstrate a chat interaction with a CodeGPT agent

async def chat_example(prompt):
    # Retrieve the CodeGPT API key from environment variables
    CODEGPT_API_KEY = os.getenv("CODEGPT_API_KEY")

    # Retrieve the CodeGPT agent ID from environment variables (or you can provide it directly)
    # You can also specify the agent ID directly
    CODEGPT_AGENT_ID = os.getenv("CODEGPT_AGENT_ID")

    print(CODEGPT_API_KEY)
    print(CODEGPT_AGENT_ID)
    # Create an instance of the CodeGPT agent using the API key and agent ID
    agent_instance = Agent(api_key=CODEGPT_API_KEY, agent_id=CODEGPT_AGENT_ID)

    # Use an asynchronous loop to interact with the agent and get responses
    async for response in agent_instance.chat_completion(prompt, stream=True):
        print(response)  # Print the responses obtained from the agent

# Entry point of the script
if __name__ == "__main__":
    text = "First President of USA?"  # Define a user message for the conversation
    prompt = {"role": "user", "content": text}  # Create a prompt for the user

    # Run the chat_example function with the user's prompt using asyncio
    asyncio.run(chat_example(prompt))
