from app.config import REFUSAL_MESSAGE


def build_mcq_prompt(question, options, retrieved_chunks):
    context = "\n\n".join([chunk["chunk"]["text"] for chunk in retrieved_chunks[:3]])

    options_text = "\n".join([f"{k}. {v}" for k, v in options.items()])

    prompt = f"""
You are an aviation exam assistant.

Answer the multiple-choice question using ONLY the retrieved text.

If none of the options are supported by the retrieved text,
respond exactly with:
"{REFUSAL_MESSAGE}"

Retrieved Text:
{context}

Question:
{question}

Options:
{options_text}

Return ONLY the correct option letter (A, B, C, or D).
Do not explain.
"""

    return prompt