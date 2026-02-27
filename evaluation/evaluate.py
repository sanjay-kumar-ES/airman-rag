import json
from app.ask import ask_mcq
from app.retrieval.index import load_faiss_index
from app.retrieval.search import search_index
from app.config import REFUSAL_MESSAGE, SIMILARITY_THRESHOLD


def evaluate():
    with open("evaluation/questions.json", "r") as f:
        questions = json.load(f)

    index, metadata = load_faiss_index()

    total = len(questions)
    answered = 0
    refused = 0
    hallucinations = 0
    similarity_scores = []

    print("\nRunning MCQ Evaluation...\n")

    for q in questions:
        print("=" * 70)
        print(f"Q{q['id']}: {q['question']}\n")

        # Print options
        for key, value in q["options"].items():
            print(f"{key}. {value}")

        # Retrieve top chunk for similarity analysis
        results = search_index(index, metadata, q["question"])

        if results:
            top_score = results[0]["score"]
            similarity_scores.append(top_score)
        else:
            top_score = 0

        # Ask model
        model_answer = ask_mcq(q["question"], q["options"])

        print("\nModel Answer:", model_answer)
        print(f"Top Similarity Score: {top_score:.3f}")

        # Classification
        if model_answer == REFUSAL_MESSAGE:
            print("Result: x Refused")
            refused += 1
        else:
            answered += 1

            if top_score < SIMILARITY_THRESHOLD:
                hallucinations += 1
                print("Result:  Hallucination (Low Similarity)")
            else:
                print("Result:Correct Answer")

        # Show citation preview
        if results:
            top_chunk = results[0]["chunk"]
            print(f"Citation: {top_chunk['doc']} (Page {top_chunk['page']})")

        print()

    # Summary statistics
    avg_similarity = (
        sum(similarity_scores) / len(similarity_scores)
        if similarity_scores else 0
    )

    answer_rate = (answered / total) * 100 if total > 0 else 0
    hallucination_rate = (hallucinations / total) * 100 if total > 0 else 0

    print("\n" + "=" * 70)
    print("Evaluation Summary")
    print("=" * 70)
    print(f"Total Questions: {total}")
    print(f"Answered: {answered}")
    print(f"Refused: {refused}")
    print(f"Answer Rate: {answer_rate:.2f}%")
    print(f"Average Top Similarity Score: {avg_similarity:.3f}")
    print(f"Hallucinations: {hallucinations}")
    print(f"Hallucination Rate: {hallucination_rate:.2f}%")
    print("=" * 70)


if __name__ == "__main__":
    evaluate()