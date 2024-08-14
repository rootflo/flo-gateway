import requests
from dataclasses import dataclass
from fastapi import HTTPException

@dataclass
class BaseLLMConfig():
     endpoint: str

class BaseLLMService:
    def __init__(self, endpoint: str) -> None:
        self.endpoint = endpoint

    def chat_completion(self, payload, headers, params) -> requests.Response:
        response: requests.Response = requests.post(self.endpoint, json=payload,
                                                     headers=headers, params=params)
        if response.status_code != 200:
                raise HTTPException(status_code=response.status_code, detail=response.text)
        return response