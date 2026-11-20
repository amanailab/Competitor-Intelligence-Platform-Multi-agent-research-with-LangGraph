
from pydantic import BaseModel, Field, HttpUrl


class SourceEvidence(BaseModel):

    title: str = Field(
        description="Title of the source"
    )

    url: HttpUrl = Field(
        description="Valid source URL"
    )

    evidence: str = Field(
        description="Relevant text supporting the claim"
    )

    source_type: str = Field(
        description="Official, news, research, or other"
    )


class ResearchClaim(BaseModel):

    claim: str

    sources: list[SourceEvidence] = Field(
        default_factory=list
    )

    is_supported: bool = False

    validation_notes: str = ""
