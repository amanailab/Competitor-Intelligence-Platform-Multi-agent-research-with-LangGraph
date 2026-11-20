
from tools.source_validator import validate_research_claim


claim = "Netflix provides streaming subscription plans."

sources = [
    {
        "title": "Netflix Official Website",
        "url": "https://www.netflix.com",
        "evidence": "Netflix offers movies and TV shows through subscriptions.",
        "source_type": "Official"
    },
    {
        "title": "Example News Source",
        "url": "https://example.com",
        "evidence": "An example source for testing.",
        "source_type": "News"
    }
]


result = validate_research_claim(
    claim=claim,
    sources=sources
)


print("\nSOURCE VALIDATION RESULT\n")

print(result.model_dump_json(indent=4))

print("\nSupported:", result.is_supported)
