# src/vector/semantic_search_service.py

from src.vector.vector_store import (
    VectorStore
)


class SemanticSearchService:

    def __init__(self):

        self.store = (
            VectorStore()
        )

    def search(
        self,
        query: str,
        k: int = 5
    ):

        return (
            self.store
            .similarity_search(
                query,
                k
            )
        )