
import os
from dotenv import load_dotenv
from tavily import TavilyClient

# Step 1: Load credentials
load_dotenv()

# Step 2: Initialize Tavily
tavily = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)

# Step 3: Define a research query
query = """
Netflix company overview, products,
streaming services and recent developments
"""

# Step 4: Search the web
response = tavily.search(
    query=query,
    max_results=5
)

# Step 5: Display results
print("\n===== RESEARCH RESULTS =====\n")

for index, result in enumerate(response["results"], start=1):

    print(f"\nResult {index}")
    print("Title:", result["title"])
    print("URL:", result["url"])
    print("Content:", result["content"])
    print("-" * 60)
