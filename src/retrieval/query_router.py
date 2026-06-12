from src.retrieval.json_query_engine import (
    JSONQueryEngine
)


class QueryRouter:

    def __init__(self):

        self.engine = (
            JSONQueryEngine()
        )

    def route(
        self,
        query: str
    ):

        query = (
            query.strip()
        )

        return {
            "message":
            (
                "Router will be "
                "expanded in Phase 10"
            ),
            "query": query
        }