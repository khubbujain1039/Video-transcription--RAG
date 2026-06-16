# 🎥 Video Agentic RAG using Qwen2.5, Whisper & LangGraph

## 📌 Overview

Video Agentic RAG is an AI-powered application that allows users to upload a YouTube video URL, automatically transcribe the video, build a searchable knowledge base, and ask natural language questions about the video's content.

The system combines Speech-to-Text, Vector Search, Retrieval-Augmented Generation (RAG), and Agentic Workflows to provide accurate answers grounded in the video transcript.

---

## 🚀 Features

* Download videos directly from YouTube using yt-dlp
* Automatic speech-to-text transcription using OpenAI Whisper
* Audio processing with FFmpeg
* Transcript cleaning and preprocessing
* Semantic embeddings using Sentence Transformers
* Vector storage using ChromaDB
* Retrieval-Augmented Generation (RAG)
* Agentic workflow orchestration using LangGraph
* Local LLM inference using Qwen2.5 through Ollama
* Interactive Streamlit chat interface
* Video summarization support

---

## 🏗️ System Architecture

```text
YouTube URL
     │
     ▼
yt-dlp
(Video Download)
     │
     ▼
FFmpeg
(Audio Processing)
     │
     ▼
Whisper
(Speech-to-Text)
     │
     ▼
Text Cleaning
     │
     ▼
Embeddings
(MiniLM-L6-v2)
     │
     ▼
ChromaDB
(Vector Database)
     │
     ▼
LangGraph Agent
 ┌──────────────┐
 │   Router     │
 └──────┬───────┘
        │
   ┌────┴────┐
   ▼         ▼
Retrieve  Summary
   │         │
   └────┬────┘
        ▼
    Generate
        ▼
      Answer
```

---

## 📂 Project Structure

```text
Video transcription-RAG/
│
├── app.py
│
├── agents/
│   └── graph.py
│
├── utils/
│   ├── video_loader.py
│   ├── transcriber.py
│   ├── embeddings.py
│   ├── vector_store.py
│   └── text_cleaner.py
│
├── chroma_db/
│
├── downloads/
│
└── requirements.txt
```

---

## 📄 File Descriptions

### app.py

Main Streamlit application.

Responsibilities:

* Accept YouTube URLs
* Download videos
* Generate transcripts
* Build vector database
* Handle user chat
* Execute LangGraph workflow
* Display answers

---

### utils/video_loader.py

Downloads videos using yt-dlp.

Responsibilities:

* Download YouTube content
* Store files locally
* Return downloaded file path

---

### utils/transcriber.py

Handles speech-to-text conversion.

Responsibilities:

* Load Whisper model
* Use FFmpeg for audio processing
* Generate transcript
* Produce timestamped segments

---

### utils/text_cleaner.py

Preprocesses transcript text.

Responsibilities:

* Remove URLs
* Remove tabs and extra spaces
* Normalize text

---

### utils/embeddings.py

Generates semantic embeddings.

Model:

```python
sentence-transformers/all-MiniLM-L6-v2
```

Responsibilities:

* Convert text into vectors
* Enable semantic search

---

### utils/vector_store.py

Creates ChromaDB vector database.

Responsibilities:

* Convert transcript segments into LangChain Documents
* Generate embeddings
* Store vectors in ChromaDB

---

### agents/graph.py

Agentic workflow implementation using LangGraph.

Nodes:

* Router
* Retrieve
* Summary
* Generate

Responsibilities:

* Decide workflow path
* Retrieve relevant transcript chunks
* Summarize transcripts
* Generate final answers

---

## 🤖 Agent Workflow

### Router Node

Determines whether the user request requires:

* Retrieval
* Summarization

### Retrieve Node

Searches ChromaDB for relevant transcript chunks.

### Summary Node

Generates concise video summaries.

### Generate Node

Uses Qwen2.5 to generate the final response.

---

## 🛠️ Technologies Used

### Frontend

* Streamlit

### Video Processing

* yt-dlp
* FFmpeg

### Speech Recognition

* OpenAI Whisper

### Embeddings

* Sentence Transformers
* all-MiniLM-L6-v2

### Vector Database

* ChromaDB

### LLM

* Qwen2.5 (via Ollama)

### Agent Framework

* LangGraph

### AI Framework

* LangChain

---

## 📦 Installation

### Clone Repository

```bash
git clone <repository-url>
cd Video-transcription-RAG
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Install Ollama

Pull Qwen2.5 model:

```bash
ollama pull qwen2.5:7b
```

### Install FFmpeg

Verify installation:

```bash
ffmpeg -version
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

---

## 💬 Example Queries

### Question Answering

```text
What is reinforcement learning?
```

```text
What are the key points discussed in the video?
```

```text
Explain the transformer architecture mentioned in the lecture.
```

### Summarization

```text
Summarize this video.
```

```text
Give an overview of the video.
```

---

## 🔍 Retrieval-Augmented Generation Pipeline

1. Download video
2. Transcribe audio using Whisper
3. Clean transcript
4. Generate embeddings
5. Store vectors in ChromaDB
6. Retrieve relevant chunks
7. Generate grounded responses using Qwen2.5

---

## 📈 Future Enhancements

* Hybrid Search (BM25 + Vector Search)
* LLM-based Router
* Web Search Integration
* Timestamp-based Answers
* Multi-Video Knowledge Base
* Conversation Memory
* Streaming Responses
* Source Citations

---

## 🎯 Learning Outcomes

This project demonstrates:

* Agentic RAG
* LangGraph Workflows
* Semantic Search
* Vector Databases
* Speech-to-Text Systems
* LLM Integration
* Retrieval-Augmented Generation
* End-to-End AI Application Development

---

## 👨‍💻 Author

Khushboo Jain

Built as a practical implementation of Agentic RAG for video understanding and question answering using modern open-source AI technologies.
