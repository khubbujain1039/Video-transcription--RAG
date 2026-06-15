from langchain_core.documents import Document

from langchain_chroma import Chroma

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from utils.embeddings import (
    get_embeddings
)

from utils.text_cleaner import (
    clean_text
)


def build_vectordb(
    result,
    video_url
):
    """
    Creates ChromaDB vector store
    from cleaned transcript chunks.
    """

    full_text = clean_text(
        result["text"]
    )

    splitter = (
        RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
    )

    chunks = splitter.split_text(
        full_text
    )

    docs = []

    for i, chunk in enumerate(
        chunks
    ):

        docs.append(
            Document(
                page_content=chunk,

                metadata={
                    "chunk_id": i,
                    "source": video_url
                }
            )
        )

    vectordb = (
        Chroma.from_documents(
            documents=docs,

            embedding=
            get_embeddings(),

            persist_directory=
            "chroma_db"
        )
    )

    return vectordb