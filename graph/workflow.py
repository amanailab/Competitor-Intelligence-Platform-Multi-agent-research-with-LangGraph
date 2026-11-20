
from langgraph.graph import StateGraph, START, END

from graph.state import CompetitorIntelligenceState

from agents.market_research_agent import run_market_research
from agents.product_analysis_agent import run_product_analysis
from agents.pricing_intelligence_agent import run_pricing_analysis
from agents.swot_analysis_agent import run_swot_analysis

from utils.agent_executor import execute_agent


# ==========================================
# NODE 1: MARKET RESEARCH
# ==========================================

def market_research_node(state: CompetitorIntelligenceState):

    print("\n[1/5] Running Market Research Agent...")

    execution = execute_agent(
        run_market_research,
        state["company"]
    )

    if not execution["success"]:
        raise RuntimeError(
            f"Market Research failed: {execution['error']}"
        )

    return {
        "market_research": execution["result"]
    }


# ==========================================
# NODE 2: PRODUCT ANALYSIS
# ==========================================

def product_analysis_node(state: CompetitorIntelligenceState):

    print("\n[2/5] Running Product Analysis Agent...")

    execution = execute_agent(
        run_product_analysis,
        state["company"],
        state["competitors"]
    )

    if not execution["success"]:
        raise RuntimeError(
            f"Product Analysis failed: {execution['error']}"
        )

    return {
        "product_analysis": execution["result"]
    }


# ==========================================
# NODE 3: PRICING INTELLIGENCE
# ==========================================

def pricing_intelligence_node(state: CompetitorIntelligenceState):

    print("\n[3/5] Running Pricing Intelligence Agent...")

    execution = execute_agent(
        run_pricing_analysis,
        state["company"],
        state["competitors"],
        state["country"]
    )

    if not execution["success"]:
        raise RuntimeError(
            f"Pricing Intelligence failed: {execution['error']}"
        )

    return {
        "pricing_analysis": execution["result"]
    }


# ==========================================
# NODE 4: SWOT ANALYSIS
# ==========================================

def swot_analysis_node(state: CompetitorIntelligenceState):

    print("\n[4/5] Running SWOT Analysis Agent...")

    research_context = f"""
    MARKET RESEARCH:
    {state["market_research"]}

    PRODUCT ANALYSIS:
    {state["product_analysis"]}

    PRICING ANALYSIS:
    {state["pricing_analysis"]}
    """

    execution = execute_agent(
        run_swot_analysis,
        state["company"],
        state["competitors"],
        research_context
    )

    if not execution["success"]:
        raise RuntimeError(
            f"SWOT Analysis failed: {execution['error']}"
        )

    return {
        "swot_analysis": execution["result"]
    }


# ==========================================
# NODE 5: FINAL REPORT
# ==========================================

def final_report_node(state: CompetitorIntelligenceState):

    print("\n[5/5] Generating Final Report...")

    report = f"""
==================================================
          COMPETITOR INTELLIGENCE REPORT
==================================================

COMPANY: {state["company"]}

COMPETITORS: {", ".join(state["competitors"])}

COUNTRY: {state["country"]}

RESEARCH OBJECTIVE:
{state["research_objective"]}


==================================================
                  MARKET RESEARCH
==================================================

{state["market_research"]}


==================================================
                  PRODUCT ANALYSIS
==================================================

{state["product_analysis"]}


==================================================
                PRICING INTELLIGENCE
==================================================

{state["pricing_analysis"]}


==================================================
                   SWOT ANALYSIS
==================================================

{state["swot_analysis"]}


==================================================
                    END OF REPORT
==================================================
"""

    return {
        "final_report": report
    }


# ==========================================
# BUILD LANGGRAPH
# ==========================================

builder = StateGraph(CompetitorIntelligenceState)

builder.add_node("market_research", market_research_node)
builder.add_node("product_analysis", product_analysis_node)
builder.add_node("pricing_intelligence", pricing_intelligence_node)
builder.add_node("swot_analysis", swot_analysis_node)
builder.add_node("final_report", final_report_node)


# Sequential execution

builder.add_edge(START, "market_research")

builder.add_edge("market_research", "product_analysis")

builder.add_edge("product_analysis", "pricing_intelligence")

builder.add_edge("pricing_intelligence", "swot_analysis")

builder.add_edge("swot_analysis", "final_report")

builder.add_edge("final_report", END)


# Compile graph

competitor_intelligence_graph = builder.compile()


# ==========================================
# RUN COMPLETE WORKFLOW
# ==========================================

def run_competitor_intelligence(
    company: str,
    competitors: list[str],
    country: str,
    research_objective: str
):

    initial_state = {
        "company": company,
        "competitors": competitors,
        "country": country,
        "research_objective": research_objective,

        "market_research": "",
        "product_analysis": "",
        "pricing_analysis": "",
        "swot_analysis": "",
        "final_report": ""
    }

    result = competitor_intelligence_graph.invoke(
        initial_state
    )

    return result


# ==========================================
# MAIN
# ==========================================

if __name__ == "__main__":

    result = run_competitor_intelligence(
        company="Netflix",

        competitors=[
            "Amazon Prime Video",
            "Disney+"
        ],

        country="India",

        research_objective=(
            "Analyze market position, products, pricing "
            "and competitive strengths."
        )
    )

    print("\n\n")
    print(result["final_report"])
