
from typing import Any


def evaluate_agent_output(
    agent_name: str,
    output: Any,
    required_keywords: list[str] | None = None,
    minimum_length: int = 100
):

    text = str(output).strip()

    # 1. Check whether output exists
    has_output = bool(text)

    # 2. Check output length
    sufficient_length = len(text) >= minimum_length

    # 3. Check required topics
    if required_keywords:
        missing_keywords = [
            keyword
            for keyword in required_keywords
            if keyword.lower() not in text.lower()
        ]
    else:
        missing_keywords = []

    topic_coverage = (
        len(missing_keywords) == 0
    )

    # 4. Check whether source references are present
    has_sources = (
        "http://" in text.lower()
        or "https://" in text.lower()
    )

    # 5. Calculate a simple structural score
    checks = [
        has_output,
        sufficient_length,
        topic_coverage,
        has_sources
    ]

    score = round(
        sum(checks) / len(checks) * 100,
        2
    )

    return {
        "agent_name": agent_name,
        "score": score,
        "has_output": has_output,
        "sufficient_length": sufficient_length,
        "topic_coverage": topic_coverage,
        "has_sources": has_sources,
        "missing_keywords": missing_keywords
    }


def print_evaluation_report(results):

    print("\n========== AGENT EVALUATION ==========")

    for result in results:

        print(f"\nAgent: {result['agent_name']}")

        print(f"Score: {result['score']}%")

        print(f"Output available: {result['has_output']}")

        print(
            f"Length check: {result['sufficient_length']}"
        )

        print(
            f"Topic coverage: {result['topic_coverage']}"
        )

        print(
            f"Sources present: {result['has_sources']}"
        )

        print(
            f"Missing topics: {result['missing_keywords']}"
        )

    print("\n======================================")
