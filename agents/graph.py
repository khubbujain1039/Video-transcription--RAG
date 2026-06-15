from typing import TypedDict

from langgraph.graph import StateGraph, END
from langchain_ollama import ChatOllama


class GraphState(TypedDict):
    question: str
    context: str
    answer: str
    route: str
    retriever: object


# ---------------- ROUTER ----------------
def router(state):
    q = state["question"].lower()

    if any(x in q for x in ["summary", "summarize", "overview", "key points"]):
        return {"route": "summary"}

    return {"route": "retrieve"}


# ---------------- RETRIEVE ----------------
def retrieve(state):

    retriever = state["retriever"]

    docs = retriever.invoke(state["question"])

    context = "\n\n".join([d.page_content for d in docs])

    return {"context": context}


# ---------------- SUMMARY ----------------
def summary(state):

    llm = ChatOllama(model="qwen2.5:7b", temperature=0)

    transcript = state.get("context", "")

    response = llm.invoke(
        f"""
Summarize this transcript:

{transcript[:12000]}
"""
    )

    return {"context": response.content}


# ---------------- GENERATE ----------------
def generate(state):

    llm = ChatOllama(model="qwen2.5:7b", temperature=0)

    prompt = f"""
You are a helpful assistant.

Context:
{state['context']}

Question:
{state['question']}

Answer:
"""

    response = llm.invoke(prompt)

    return {"answer": response.content}


# ---------------- ROUTE DECISION ----------------
def route_decision(state):
    return state["route"]


# ---------------- BUILD GRAPH ----------------
def build_graph():

    graph = StateGraph(GraphState)

    graph.add_node("router", router)
    graph.add_node("retrieve", retrieve)
    graph.add_node("summary", summary)
    graph.add_node("generate", generate)

    graph.set_entry_point("router")

    graph.add_conditional_edges(
        "router",
        route_decision,
        {
            "retrieve": "retrieve",
            "summary": "summary"
        }
    )

    graph.add_edge("retrieve", "generate")
    graph.add_edge("summary", "generate")
    graph.add_edge("generate", END)

    return graph.compile()