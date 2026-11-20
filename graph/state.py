
from typing import TypedDict


class CompetitorIntelligenceState(TypedDict):

    # User input
    company: str
    competitors: list[str]
    country: str
    research_objective: str

    # Specialist agent outputs
    market_research: str
    product_analysis: str
    pricing_analysis: str
    swot_analysis: str

    # Final output
    final_report: str
