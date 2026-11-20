
from pydantic import BaseModel, Field
from typing import List


class CompanyOverview(BaseModel):
    company_name: str = Field(
        description="Name of the company"
    )

    industry: str = Field(
        description="Industry in which the company operates"
    )

    business_model: str = Field(
        description="How the company generates revenue"
    )

    headquarters: str = Field(
        description="Company headquarters"
    )


class ProductInformation(BaseModel):
    product_name: str

    features: List[str]

    strengths: List[str]

    weaknesses: List[str]


class PricingInformation(BaseModel):
    product_name: str

    plan_name: str

    price: str

    billing_period: str

    currency: str


class SWOTAnalysis(BaseModel):
    strengths: List[str]

    weaknesses: List[str]

    opportunities: List[str]

    threats: List[str]


class CompetitorIntelligenceReport(BaseModel):
    company_overview: CompanyOverview

    products: List[ProductInformation]

    pricing: List[PricingInformation]

    swot: SWOTAnalysis

    key_recommendations: List[str]
