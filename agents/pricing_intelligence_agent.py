
import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from tools.web_search import web_search


# 1. Load environment variables
load_dotenv()




llm = ChatGoogleGenerativeAI(
    model=os.getenv("GOOGLE_MODEL", "gemini-3.5-flash-lite"),
    max_retries=3
)


# 3. Define agent instructions
SYSTEM_PROMPT = """
You are an expert Pricing Intelligence Analyst.

Your responsibility is to research and compare
company subscription and product pricing.

Your tasks:

1. Identify subscription plans.
2. Research monthly and annual prices.
3. Identify pricing tiers.
4. Compare regional pricing.
5. Identify premium and basic plans.
6. Research bundles and offers.
7. Analyze value propositions.

Research guidelines:

- Use web_search to collect current evidence.
- Prefer official company pricing pages.
- Consider the specified country.
- Never invent prices.
- Mention currency explicitly.
- Include the retrieval date.
- Distinguish missing information from
  unavailable plans.
- Include source URLs.

Return the report using these sections:

1. Pricing Overview
2. Subscription Plans
3. Pricing Comparison
4. Regional Differences
5. Bundles and Offers
6. Value for Money
7. Pricing Insights
8. Sources
"""


# 4. Create Pricing Intelligence Agent
pricing_intelligence_agent = create_agent(
    model=llm,
    tools=[web_search],
    system_prompt=SYSTEM_PROMPT,
    name="pricing_intelligence_agent"
)


# 5. Define execution function
def run_pricing_analysis(
    company: str,
    competitors: list[str],
    country: str
):

    competitor_names = ", ".join(competitors)

    user_request = f"""
    Conduct pricing intelligence research.

    Main Company: {company}

    Competitors: {competitor_names}

    Country: {country}

    Research subscription plans, monthly and
    annual pricing, tiers, bundles and value.

    Compare all companies using current
    and verifiable information.

    Include currency and source URLs.
    """

    result = pricing_intelligence_agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": user_request
                }
            ]
        }
    )

    return result["messages"][-1].content


# 6. Independent testing
if __name__ == "__main__":

    report = run_pricing_analysis(
        company="Netflix",
        competitors=[
            "Amazon Prime Video",
            "Disney+"
        ],
        country="India"
    )

    print("\n===== PRICING INTELLIGENCE REPORT =====\n")
    print(report)
