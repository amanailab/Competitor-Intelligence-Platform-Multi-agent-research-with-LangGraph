
from schemas.competitor_schema import (
    CompanyOverview,
    ProductInformation,
    PricingInformation,
    SWOTAnalysis,
    CompetitorIntelligenceReport
)


report = CompetitorIntelligenceReport(

    company_overview=CompanyOverview(
        company_name="Netflix",
        industry="Entertainment",
        business_model="Subscription-based streaming",
        headquarters="California, USA"
    ),

    products=[
        ProductInformation(
            product_name="Netflix Streaming",
            features=[
                "Movies",
                "TV Shows",
                "Original Content"
            ],
            strengths=[
                "Large content library"
            ],
            weaknesses=[
                "Subscription cost"
            ]
        )
    ],

    pricing=[
        PricingInformation(
            product_name="Netflix",
            plan_name="Premium",
            price="649",
            billing_period="Monthly",
            currency="INR"
        )
    ],

    swot=SWOTAnalysis(
        strengths=["Strong brand"],
        weaknesses=["High content costs"],
        opportunities=["New markets"],
        threats=["Competition"]
    ),

    key_recommendations=[
        "Improve regional content",
        "Optimize subscription pricing"
    ]
)


print(report.model_dump_json(indent=4))
