from langchain.tools import tool
import requests

@tool
def search(query: str) -> str:
    """Search the web for recent info."""
    url = f"https://www.google.com/search?q={query}"
    return f"Use this link to check: {url}"
