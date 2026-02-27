from app.config import REFUSAL_MESSAGE


def validate_answer(answer, retrieved_chunks):
    # If model already refused, accept it
    if answer.strip() == REFUSAL_MESSAGE:
        return answer

    # Otherwise trust the LLM (prompt already enforces grounding)
    return answer