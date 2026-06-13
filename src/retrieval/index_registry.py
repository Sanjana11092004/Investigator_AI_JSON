from src.retrieval.index_builder import (
    IndexBuilder
)


class IndexRegistry:

    _index = (
        IndexBuilder()
        .build()
    )

    @classmethod
    def get_index(cls):

        return cls._index

    @classmethod
    def refresh(cls):

        cls._index = (
            IndexBuilder()
            .build()
        )

        return cls._index