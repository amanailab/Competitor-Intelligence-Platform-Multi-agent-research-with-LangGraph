
from urllib.parse import urlparse

from schemas.source_schema import (
    ResearchClaim,
    SourceEvidence
)


def validate_source_url(url: str) -> bool:

    try:
        parsed_url = urlparse(str(url))

        return (
            parsed_url.scheme in ["http", "https"]
            and bool(parsed_url.netloc)
        )

    except Exception:
        return False


def validate_research_claim(
    claim: str,
    sources: list[dict]
) -> ResearchClaim:

    valid_sources = []

    for source in sources:

        try:
            evidence = SourceEvidence(**source)

            if validate_source_url(str(evidence.url)):
                valid_sources.append(evidence)

        except Exception as error:
            print("Invalid source:", error)

    is_supported = (
        len(valid_sources) > 0
        and any(
            len(source.evidence.strip()) > 0
            for source in valid_sources
        )
    )

    return ResearchClaim(
        claim=claim,
        sources=valid_sources,
        is_supported=is_supported,
        validation_notes=(
            "At least one source with evidence was provided."
            if is_supported
            else "No valid source evidence was provided."
        )
    )
