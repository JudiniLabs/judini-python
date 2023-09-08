import os
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from judini.codegpt.agent import Agent
from judini.codegpt.alias import *

from dotenv import load_dotenv

load_dotenv()


app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello": "World"}

class Item(BaseModel):
    text: str



@app.post("/prompt/")
async def read_prompt(item: Item):
    prompt = item.text
    codegpt_api_key = os.getenv("CODEGPT_API_KEY")
    codegpt_agent_id = os.getenv("CODEGPT_AGENT_ID")

    agent = Agent(api_key=codegpt_api_key, agent_id=codegpt_agent_id)

    generator = agent.chat_completion(prompt, stream=True)
    return StreamingResponse(generator)