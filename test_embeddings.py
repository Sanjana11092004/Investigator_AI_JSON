from src.vector.embedding_service import (
    EmbeddingService
)

print("STEP 1")

model = (
    EmbeddingService()
    .get_model()
)

print("STEP 2")

vector = (
    model.embed_query(
        "liver toxicity"
    )
)

print("STEP 3")

print(
    "VECTOR LENGTH:",
    len(vector)
)

print(
    "\nFIRST 10 VALUES:"
)

print(
    vector[:10]
)