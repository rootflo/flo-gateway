from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate

# Define the base URL for the custom LLM endpoint
base_url = "http://localhost:8000/llm/"

# Initialize the LLM with the custom endpoint
llm = OpenAI(base_url=base_url)

# Define a prompt template
prompt = PromptTemplate(
    input_variables=["topic"],
    template="Tell me a story about advebnture."
)

# Create an LLM chain

llm_chain = llm

# Run the LLM chain
response = llm_chain.invoke("Hi, how are you")
print(response)
