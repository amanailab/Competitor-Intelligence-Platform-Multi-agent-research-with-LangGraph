
import os
import json

from dotenv import load_dotenv
from tavily import TavilyClient
from langchain_core.tools import tool

load_dotenv()

tavily_client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)


@tool
def web_search(query: str) -> str:
    """
    Search the web for company and market
    information. Return concise research evidence.
    """

    try:
        response = tavily_client.search(
            query=query,
            max_results=3,
            search_depth="basic"
        )

        results = []

        for item in response.get("results", []):

            results.append({
                "title": item.get("title"),
                "url": item.get("url"),
                "content": (item.get("content") or "")[:200]
            })

        return json.dumps(
            results,
            indent=2
        )

    except Exception as e:
        return json.dumps({
            "error": str(e)
        })
