from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("url-shortener")
CLEANURI_API_URL = "https://cleanuri.com/api/v1/shorten"

async def shorten_url(original_url: str) -> str | None:
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {"url": original_url}

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(CLEANURI_API_URL, data=data, headers=headers, timeout=30.0)
            response.raise_for_status()
            result: dict[str, Any] = response.json()
            return result.get("result_url")
        except Exception as e:
            print(f"An error occurred: {e}")
            return None


@mcp.tool()
async def shorten(original_url: str) -> str | None:
    """Shorten a URL using the cleanuri API.

    Args:
        original_url: The URL to shorten.
    """
    shortened_url = await shorten_url(original_url)
    if not shortened_url:
        return "Unable to shorten the URL."
    return shortened_url

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')