import re


def clean_text(text):
    # Remove multiple newlines
    text = re.sub(r"\n+", "\n", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    # Strip leading/trailing whitespace
    text = text.strip()

    return text