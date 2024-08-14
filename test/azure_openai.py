from langchain_openai import AzureChatOpenAI, AzureOpenAI
from dotenv import load_dotenv
load_dotenv()
import os

# Set up the LangChain AzureOpenAI model to use the FastAPI gateway
llm = AzureChatOpenAI(
    azure_endpoint="http://localhost:8000/gateway/gpt-4",
    model_name="gpt-4",  # Example model name; use the model you have deployed
    temperature=0.7,
    max_tokens=150,
    api_version="2023-03-15-preview",
    api_key=os.getenv("AZURE_OPEN_AI_KEY")
)

# Example prompt
for chunck in llm.stream("I love you"):
    print(chunck)
