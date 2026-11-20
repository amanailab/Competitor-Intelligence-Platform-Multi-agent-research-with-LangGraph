
import os
from dotenv import load_dotenv

from pydantic import BaseModel, Field

from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()


# ----------------------------------
# STEP 1: DEFINE OUTPUT SCHEMA
# ----------------------------------

class ProductAnalysis(BaseModel):

    company_name: str = Field(
        description="Name of the company"
    )

    products: list[str] = Field(
        description="Important products offered by the company"
    )

    features: list[str] = Field(
        description="Important product features"
    )

    strengths: list[str] = Field(
        description="Product strengths"
    )

    weaknesses: list[str] = Field(
        description="Product weaknesses"
    )

    competitive_advantages: list[str] = Field(
        description="Competitive advantages of the products"
    )


# ----------------------------------
# STEP 2: INITIALIZE GEMINI
# ----------------------------------

llm = ChatGoogleGenerativeAI(
    model=os.getenv("GOOGLE_MODEL", "gemini-3.5-flash-lite"),
    max_retries=3
)


# ----------------------------------
# STEP 3: ENABLE STRUCTURED OUTPUT
# ----------------------------------

structured_llm = llm.with_structured_output(
    ProductAnalysis
)


# ----------------------------------
# STEP 4: SEND USER QUERY
# ----------------------------------

response = structured_llm.invoke(
    """
    Analyze Netflix as a company.

    Identify its important products, product features,
    strengths, weaknesses and competitive advantages.

    Return factual and concise information.
    Do not invent specific facts.
    """
)


# ----------------------------------
# STEP 5: DISPLAY STRUCTURED RESULT
# ----------------------------------

print("\nSTRUCTURED PRODUCT ANALYSIS\n")

print(response.model_dump_json(indent=4))


# ----------------------------------
# STEP 6: ACCESS INDIVIDUAL FIELDS
# ----------------------------------

print("\nCOMPANY:", response.company_name)

print("\nPRODUCTS:")

for product in response.products:
    print("-", product)
