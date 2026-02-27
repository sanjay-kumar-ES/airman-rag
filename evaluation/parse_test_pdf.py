import fitz
import re
import json


def extract_mcqs(pdf_path):
    doc = fitz.open(pdf_path)
    full_text = ""

    for page in doc:
        full_text += page.get_text("text") + "\n"

    doc.close()

    # Stop before answer key if present
    if "Answer" in full_text:
        full_text = full_text.split("Answer")[0]

    # Pattern for MCQ blocks
    pattern = r"(\d+)\.\s*(.*?)\s*A\.\s*(.*?)\s*B\.\s*(.*?)\s*C\.\s*(.*?)\s*D\.\s*(.*?)(?=\n\d+\.|\Z)"

    matches = re.findall(pattern, full_text, re.DOTALL)

    questions = []

    for match in matches:
        q_id, question, A, B, C, D = match

        questions.append({
            "id": int(q_id),
            "question": question.strip().replace("\n", " "),
            "options": {
                "A": A.strip().replace("\n", " "),
                "B": B.strip().replace("\n", " "),
                "C": C.strip().replace("\n", " "),
                "D": D.strip().replace("\n", " ")
            }
        })

    return questions


if __name__ == "__main__":
    pdf_path = "evaluation/test_questions.pdf"

    questions = extract_mcqs(pdf_path)

    with open("evaluation/questions.json", "w") as f:
        json.dump(questions, f, indent=2)

    print(f"Extracted {len(questions)} MCQs.")