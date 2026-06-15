from src.vector.semantic_search_service import (
    SemanticSearchService
)

print("STEP 1")

service = (
    SemanticSearchService()
)

print("STEP 2")

results = (
    service.search(
        "heart failure"
    )
)

print("STEP 3")

for i, doc in enumerate(results):

    print(
        f"\nRESULT {i+1}"
    )

    print(
        doc.page_content[:500]
    )