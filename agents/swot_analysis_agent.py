
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


# 3. Define SWOT Agent instructions
SYSTEM_PROMPT = """
You are a Senior Business Strategy Analyst
specializing in SWOT analysis.

Your responsibility is to analyze companies
and identify strategic business factors.

Your tasks:

1. Identify company strengths.
2. Identify company weaknesses.
3. Identify market opportunities.
4. Identify external threats.
5. Analyze competitive positioning.
6. Recommend strategic improvements.

Research guidelines:

- Use web_search for relevant evidence.
- Prefer reliable and official sources.
- Use the provided research reports.
- Distinguish internal and external factors.
- Never invent company facts.
- Do not present assumptions as facts.
- Explain the reasoning behind each finding.
- Include source URLs where possible.

Return the report using these sections:

1. Company Overview
2. Strengths
3. Weaknesses
4. Opportunities
5. Threats
6. Competitive Risks
7. Strategic Recommendations
8. Sources
"""


# 4. Create SWOT Agent
swot_analysis_agent = create_agent(
    model=llm,
    tools=[web_search],
    system_prompt=SYSTEM_PROMPT,
    name="swot_analysis_agent"
)


# 5. Define execution function
def run_swot_analysis(
    company: str,
    competitors: list[str],
    research_context: str = ""
):

    competitor_names = ", ".join(competitors)

    user_request = f"""
    Perform a comprehensive SWOT analysis.

    Company: {company}

    Competitors: {competitor_names}

    Existing Research Findings:
    {research_context}

    Analyze the company's internal strengths
    and weaknesses and its external opportunities
    and threats.

    Use web search to verify relevant facts.

    Provide evidence-backed strategic
    recommendations.
    """

    result = swot_analysis_agent.invoke(
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

    report = run_swot_analysis(
        company="Netflix",
        competitors=[
            "Amazon Prime Video",
            "Disney+"
        ],
        research_context=""
    )

    print("\n===== SWOT ANALYSIS REPORT =====\n")
    print(report)
