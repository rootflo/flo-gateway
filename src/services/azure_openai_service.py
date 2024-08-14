import requests
from src.base.base_llm_service import BaseLLMConfig, BaseLLMService

class AzureOpenAIService(BaseLLMService):

    def __init__(self, config: BaseLLMConfig) -> None:
        super().__init__(config.endpoint)

    async def chat_completion(self, payload, headers, params) -> requests.Response:
        return super().chat_completion(payload, headers, params)
        