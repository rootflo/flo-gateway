from src.services.azure_openai_service import AzureOpenAIService
from src.base.base_llm_service import BaseLLMService, BaseLLMConfig
from config import gateway_config, Providers
from enum import Enum
from fastapi import HTTPException

class Service(Enum):
    AZURE = "azure"

def resolve_service(llm_name) -> BaseLLMService:
    provider: Providers = list(filter(lambda x: x.name == llm_name, gateway_config.providers))[0]
    if provider.type == Service.AZURE.value:
        return AzureOpenAIService(BaseLLMConfig(endpoint=provider.endpoint))
    else:
        raise HTTPException(status_code=404, detail="Service not found")