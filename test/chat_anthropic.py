from langchain_anthropic import ChatAnthropic
import os
from dotenv import load_dotenv
load_dotenv()

# Set up the LangChain AzureOpenAI model to use the FastAPI gateway
llm = ChatAnthropic(
    base_url="http://localhost:8000/gateway/anthropic",
    model_name="gpt-4",  # Example model name; use the model you have deployed
    temperature=0.7,
    max_tokens=150,
    api_key=os.getenv("ANTHROPIC_KEY")
)

# Example prompt
response = llm.invoke("Translate 'I love programming' to French.")
print(response)

