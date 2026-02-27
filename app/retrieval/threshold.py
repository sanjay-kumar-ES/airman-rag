from app.config import SIMILARITY_THRESHOLD


def below_threshold(results):
    if not results:
        return True

    top_score = results[0]["score"]

    return top_score < SIMILARITY_THRESHOLD