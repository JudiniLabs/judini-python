import json
from typing import List, Dict, Literal, Generator, Any
import requests

def handle_stream(response: requests.Response) -> Generator[Any, Any, Any]:
    try:
        for chunk in response.iter_content(chunk_size=64, decode_unicode=True):
            if chunk:
                yield chunk
    except Exception as e:
        print(f"Error occurred: {e}", chunk)
    finally:
        response.close()

def handle_non_stream(response: requests.Response) -> str:
    try:
        text = response.json()
        return text
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        response.close()
    