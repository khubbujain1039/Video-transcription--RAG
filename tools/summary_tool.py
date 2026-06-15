import streamlit as st

from langchain_core.tools import tool


@tool
def summarize_video(
    text: str = ""
):

    transcript = st.session_state[
        "transcript"
    ]

    return transcript[:15000]