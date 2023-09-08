
## FastAPI Judini Agent Integration

This FastAPI application demonstrates how to integrate the Judini Agent to handle chat completions.

### Setup

1.  First, you will need to install all the required packages. Ensure you have `pip` installed and run:

```bash
pip install fastapi[all] aiohttp python-dotenv` 
```

2.  Clone this repository or download the FastAPI application file.
    
3.  Set up the environment variables. This can be done by creating a `.env` file in the same directory with the following format:
    
```

CODEGPT_API_KEY=your_codegpt_api_key_here
CODEGPT_AGENT_ID=your_optional_codegpt_agent_id_here` 
```

Make sure to replace the placeholders with your actual Judini API credentials.

### Running the Application

Once the setup is complete, you can run the application using:

```bash
uvicorn main:app --reload
```
Replace `main` with the name of the file containing the FastAPI application.

### Usage

1.  Navigate to `http://localhost:8000` in your web browser. You should see a greeting message:

```json

`{"Hello": "World"}` 

```

2.  To interact with the Judini Agent, use a tool like `curl` or any API client to POST a message to the `/prompt/` endpoint:

```bash
curl -X 'POST' \
  'http://localhost:8000/prompt/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "Hello, how are you?"
}'` 
```
The response will be the completion from the Judini Agent.

### Note

This application streams the responses. If `stream` is set to `True` in the `chat_completion` method, the application will send responses as soon as they're available. If set to `False`, the application will send all responses at once after they have been collected.