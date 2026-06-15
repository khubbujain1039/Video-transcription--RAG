from langchain_core.tools import tool

from duckduckgo_search import DDGS


@tool
def web_search(
    query: str
):

    results = DDGS().text(
        query,
        max_results=5
    )

    context = ""

    for item in results:

        context += (
            item["title"]
            + "\n"
            + item["body"]
            + "\n\n"
        )

    return context