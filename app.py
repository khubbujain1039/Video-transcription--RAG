import streamlit as st

from utils.video_loader import download_video
from utils.transcriber import transcribe_video
from utils.vector_store import build_vectordb

from agents.graph import build_graph


# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Agentic Video RAG",
    layout="wide"
)

st.title("🎥 Agentic Video RAG (Qwen2.5 + LangGraph)")


# ---------------- SESSION STATE ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "processed" not in st.session_state:
    st.session_state.processed = False

if "vectordb" not in st.session_state:
    st.session_state.vectordb = None

if "transcript" not in st.session_state:
    st.session_state.transcript = ""


# ---------------- GRAPH ----------------
graph = build_graph()


# ---------------- INPUT ----------------
video_url = st.text_input("Enter YouTube URL")


# ---------------- PROCESS VIDEO ----------------
if st.button("Process Video"):

    if not video_url:
        st.warning("Please enter a YouTube URL")

    else:

        try:
            # DOWNLOAD
            with st.spinner("Downloading video..."):
                video_path = download_video(video_url)

            # TRANSCRIBE
            with st.spinner("Transcribing video..."):
                transcript_result = transcribe_video(video_path)

            transcript_text = transcript_result["text"]

            st.session_state.transcript = transcript_text

            # VECTOR DB
            with st.spinner("Building knowledge base..."):
                vectordb = build_vectordb(transcript_result, video_url)

            st.session_state.vectordb = vectordb
            st.session_state.processed = True

            st.success("Video processed successfully!")

            st.subheader("Transcript Preview")
            st.text_area("", transcript_text, height=300)

        except Exception as e:
            st.error(f"Error: {str(e)}")


# ---------------- CHAT HISTORY ----------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])


# ---------------- CHAT INPUT ----------------
question = st.chat_input("Ask anything about the video...")

if question:

    if not st.session_state.processed:
        st.warning("Please process a video first.")

    else:

        # store user message
        st.session_state.messages.append({
            "role": "user",
            "content": question
        })

        with st.chat_message("user"):
            st.write(question)

        with st.chat_message("assistant"):

            with st.spinner("Thinking..."):

                retriever = st.session_state.vectordb.as_retriever(
                    search_kwargs={"k": 5}
                )

                response = graph.invoke({
                    "question": question,
                    "retriever": retriever
                })

                answer = response["answer"]

                st.write(answer)

        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })