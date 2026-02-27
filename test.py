from app.ask import ask_question

question = "What is the Maximum Zero Fuel Mass?"
response = ask_question(question, debug=True)

print("\nAnswer:")
print(response["answer"])

print("\nCitations:")
for c in response["citations"]:
    print(c)

print("\nTop Scores:")
for r in response["retrieved_chunks"]:
    print(r["score"])