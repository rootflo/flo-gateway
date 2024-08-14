from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv
import os
load_dotenv()

# Set up the LangChain AzureOpenAI model to use the FastAPI gateway
llm = AzureChatOpenAI(
    azure_endpoint="http://localhost:8000/gateway/phi-3",
    model_name="gpt-4",  # Example model name; use the model you have deployed
    temperature=0.7,
    max_tokens=150,
    api_version="2024-02-15-preview",
    api_key=os.getenv("AZURE_ML_INFERENCE_KEY")
)

for chunck in llm.stream("I love you"):
    print(chunck)
