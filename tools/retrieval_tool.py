import streamlit as st

from langchain_core.tools import tool


@tool
def retrieve_video_context(
    question: str
):

    vectordb = st.session_state[
        "vectordb"
    ]

    retriever = vectordb.as_retriever(
        search_kwargs={
            "k": 5
        }
    )

    docs = retriever.invoke(
        question
    )

    context = "\n\n".join(
        [
            doc.page_content
            for doc in docs
        ]
    )

    return context