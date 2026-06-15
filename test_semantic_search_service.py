# test_semantic_search_service.py

from src.vector.semantic_search_service import (
    SemanticSearchService
)

service = (
    SemanticSearchService()
)

docs = (
    service.search(
        "Which patient had atrial fibrillation?"
    )
)

print(
    "RESULTS:",
    len(docs)
)

for i, doc in enumerate(
    docs,
    start=1
):

    print("\nDOC", i)
    print(
        doc.page_content[:300]
    )