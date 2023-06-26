# Judini python package

## Install

``` pip install judini ```

## Use

``` python

# import
from judini import Judini

def main():
    # Replace with your actual API key and URL ID
    api_key = "your_api_key_here"
    agent_id = "your_agent_id_here"

    # Initialize the Judini class
    judini_instance = Judini(api_key, agent_id)

    # Optional: update API key or URL ID if needed
    judini_instance.set_api_key("new_api_key")
    judini_instance.set_agent_id("new_agent_id")

    # create the user prompt
    question = "Who is the President of the United States?"

    # Make a POST request
    response = judini_instance.completion(question)

    # Handle the response as needed
    print(response)

if __name__ == "__main__":
    main()
```