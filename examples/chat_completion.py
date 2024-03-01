# Import necessary modules and libraries
import os
from judini import CodeGPTPlus
from dotenv import load_dotenv

# Load environment variables from a .env file if available
load_dotenv()


# Define a function to demonstrate a chat interaction with a CodeGPT agent

def chat_example(messages: list):
    # Retrieve the CodeGPT API key from environment variables
    CODEGPT_API_KEY = os.getenv("CODEGPT_API_KEY")
    CODEGPT_ORG_ID = os.getenv("CODEGPT_ORG_ID")
    CODEGPT_AGENT_ID = os.getenv("CODEGPT_AGENT_ID")
    # Create an instance of the CodeGPTPlus class
    codegpt = CodeGPTPlus(api_key=CODEGPT_API_KEY, org_id=CODEGPT_ORG_ID)

    # Use a loop to interact with the agent and get responses
    for chunk in codegpt.chat_completion(agent_id=CODEGPT_AGENT_ID, messages=messages, stream=True):
        print(chunk, end="")  # Print the responses obtained from the agent

# Entry point of the script
if __name__ == "__main__":
    text = "First President of USA?"  # Define a user message for the conversation
    message = {"role": "user", "content": text}  # Create a message for the user
    chat_example([message])