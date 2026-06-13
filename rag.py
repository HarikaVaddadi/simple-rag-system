from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# with open(
#     "data/insurance_policy.txt",
#     "r",
#     encoding="utf-8"
# ) as f:
#     text = f.read()
with open(
    "data/test.txt",
    "r",
    encoding="utf-8"
) as f:
    text = f.read()

chunks = text.split("\n\n")

vectorizer = TfidfVectorizer()

document_vectors = vectorizer.fit_transform(chunks)

while True:

    question = input("\nQuestion: ")

    if question.lower() == "exit":
        break

    query_vector = vectorizer.transform([question])

    scores = cosine_similarity(
        query_vector,
        document_vectors
    )

    best_idx = scores.argmax()

    print("\nRetrieved Context:")
    print(chunks[best_idx])

    print("\nAnswer:")
    print(chunks[best_idx])