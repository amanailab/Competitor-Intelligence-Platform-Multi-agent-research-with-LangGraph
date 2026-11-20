
from fastapi import FastAPI
from pydantic import BaseModel, Field

from graph.workflow import run_competitor_intelligence


# =====================================
# 1. INITIALIZE APPLICATION
# =====================================

app = FastAPI(
    title="AmanAI Lab - Competitor Intelligence",
    description="Multi-Agent AI Competitor Research System",
    version="1.0.0"
)


# =====================================
# 2. REQUEST DATA MODEL
# =====================================

class ResearchRequest(BaseModel):

    company: str = Field(min_length=1)

    competitors: list[str] = Field(min_length=1)

    country: str

    research_objective: str


# =====================================
# 3. HOME ENDPOINT
# =====================================

@app.get("/")
def home():

    return {
        "message": "Welcome to AmanAI Lab Competitor Intelligence API",
        "status": "running"
    }


# =====================================
# 4. HEALTH CHECK ENDPOINT
# =====================================

@app.get("/health")
def health_check():

    return {
        "status": "healthy",
        "service": "Competitor Intelligence API"
    }


# =====================================
# 5. RESEARCH ENDPOINT
# =====================================

@app.post("/api/v1/research")
def conduct_research(request: ResearchRequest):

    result = run_competitor_intelligence(
        company=request.company,
        competitors=request.competitors,
        country=request.country,
        research_objective=request.research_objective
    )

    return {
        "success": True,
        "company": request.company,
        "competitors": request.competitors,
        "country": request.country,
        "report": result["final_report"]
    }
