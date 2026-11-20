
from tools.web_search import web_search
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent


# Step 1: Load environment variables
load_dotenv()


load_dotenv()

llm = ChatGoogleGenerativeAI(
    model=os.getenv("GOOGLE_MODEL", "gemini-3.5-flash-lite"),
    max_retries=3
)


# Step 3: Define the agent's responsibilities
SYSTEM_PROMPT = """
You are an expert Market Research Analyst
working for a Competitive Intelligence System.

Your responsibility is to research companies
and their market position.

Your tasks:

1. Research company background.
2. Identify the industry and business model.
3. Research market trends.
4. Identify major competitors.
5. Find recent company developments.
6. Collect relevant evidence.

Instructions:

- Use the web_search tool for current information.
- Search using specific and meaningful queries.
- Never invent facts, statistics or market figures.
- Clearly identify missing information.
- Distinguish verified facts from analysis.
- Include source URLs for important findings.

Return your final research in these sections:

1. Company Overview
2. Industry Overview
3. Business Model
4. Market Position
5. Major Competitors
6. Recent Developments
7. Key Findings
8. Sources
"""


# Step 4: Create the AI agent
market_research_agent = create_agent(
    model=llm,
    tools=[web_search],
    system_prompt=SYSTEM_PROMPT,
    name="market_research_agent"
)


# Step 5: Create a function to execute the agent
def run_market_research(company: str):

    user_request = f"""
    Conduct comprehensive market research
    on the following company:

    Company: {company}

    Research its background, industry,
    business model, market position,
    competitors and recent developments.

    Use web search to collect evidence.
    """

    result = market_research_agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": user_request
                }
            ]
        }
    )

    # Extract final agent response
    final_response = result["messages"][-1]

    return final_response.content


# Step 6: Execute independently for testing
if __name__ == "__main__":

    company = "Netflix"

    report = run_market_research(company)

    print("\n========== MARKET RESEARCH REPORT ==========\n")
    print(report)
