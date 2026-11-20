
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Step 1: Load environment variables
load_dotenv()

# Step 2: Read model configuration
model_name = os.getenv("GROQ_MODEL", "openai/gpt-oss-20b")

# Step 3: Initialize the LLM
llm = ChatGroq(
    model=model_name,
    temperature=0.2,
    max_retries=2
)

# Step 4: Send a request
response = llm.invoke(
    "Explain what competitor intelligence means in business "
    "using a simple example."
)

# Step 5: Display response
print("\n===== LLM RESPONSE =====\n")
print(response.content)
