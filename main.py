from mcp.server.fastmcp import FastMCP 
import webbrowser
import urllib.parse

mcp = FastMCP("Google search")


@mcp.tool()
def open_google_search(query):
    """Open a Google search for the given query in the default web browser."""
    encoded_query = urllib.parse.quote_plus(query)
    url = f"https://www.google.com/search?q={encoded_query}"
    webbrowser.open(url)

