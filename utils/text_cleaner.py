import re


def clean_text(text: str) -> str:
    """
    Clean transcript text before
    generating embeddings.
    """

    # Remove URLs
    text = re.sub(
        r"http\S+|www\S+",
        "",
        text
    )

    # Remove HTML entities
    text = re.sub(
        r"&[a-zA-Z]+;",
        " ",
        text
    )

    # Remove multiple spaces
    text = re.sub(
        r"\s+",
        " ",
        text
    )

    # Remove extra punctuation
    text = re.sub(
        r"[^\w\s.,!?]",
        " ",
        text
    )

    return text.strip()