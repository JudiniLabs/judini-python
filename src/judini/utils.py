import json
from typing import List, Dict, Literal, Generator, Any
import requests

def handle_stream(response: requests.Response,
                  format: Literal['json', 'text']) -> Generator[Any, Any, Any]:
    try:
        for chunk in response.iter_lines():
            if chunk:
                chunk_str = chunk.decode("utf-8")
                data_array = chunk_str.replace('\n','').split('data: ')[1:]
                for jd_str in data_array:
                    if jd_str == '[DONE]':
                        break
                    json_data = json.loads(jd_str)
                    if format == 'json':
                        yield json_data
                    elif format == 'text':
                        for item in json_data['choices']:
                            yield item['delta']['content']
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        response.close()

def handle_non_stream(response: requests.Response,
                      format: Literal['json', 'text']) -> str | Dict[Any, Any]:
    try:
        json_data = response.json()
        if format == 'json':
            return json_data
        elif format == 'text':
            return json_data['choices'][0]['message']['content']
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        response.close()
    