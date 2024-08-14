from langchain_openai import AzureChatOpenAI, AzureOpenAI
from dotenv import load_dotenv
load_dotenv()
import os

# Set up the LangChain AzureOpenAI model to use the FastAPI gateway
llm = AzureChatOpenAI(
    azure_endpoint="http://localhost:8000/gateway/mixtral",
    model_name="gpt-4",  # Example model name; use the model you have deployed
    temperature=0.7,
    max_tokens=150,
    api_version="2024-02-15-preview",
    api_key=os.getenv("AZURE_ML_MIXTRAL_KEY")
)

# Example prompt
response = llm.invoke("Translate 'I love programming' to French.")
print(response)
