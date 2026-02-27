from app.generation.prompt import build_mcq_prompt
from app.generation.llm import generate_answer
from app.retrieval.search import search_index
from app.retrieval.threshold import below_threshold
from app.retrieval.index import load_faiss_index
from app.config import REFUSAL_MESSAGE


def ask_mcq(question, options, debug=False):
    index, metadata = load_faiss_index()

    results = search_index(index, metadata, question)

    if below_threshold(results):
        return REFUSAL_MESSAGE

    prompt = build_mcq_prompt(question, options, results)

    raw_answer = generate_answer(prompt).strip()

    # Clean output (sometimes model returns "A." or "A)")
    raw_answer = raw_answer.replace(".", "").replace(")", "").strip()

    if raw_answer not in options.keys():
        return REFUSAL_MESSAGE

    return raw_answer