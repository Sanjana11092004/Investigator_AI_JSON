from langchain_chroma import Chroma

from src.vector.embedding_service import (
    EmbeddingService
)


class VectorStore:

    def __init__(self):

        self.embeddings = (
            EmbeddingService()
            .get_model()
        )

        self.db = Chroma(
            collection_name=
            "clinical_narratives",

            embedding_function=
            self.embeddings,

            persist_directory=
            "vector_db"
        )

    def store_document(
        self,
        document_name,
        chunks
    ):

        ids = []

        metadata = []

        for i, chunk in enumerate(chunks):

            ids.append(
                f"{document_name}_{i}"
            )

            metadata.append({

                "document":
                document_name,

                "chunk_id":
                str(i)

            })

        self.db.add_texts(
            texts=chunks,
            metadatas=metadata,
            ids=ids
        )

    def similarity_search(
        self,
        query,
        k=5
    ):

        return (
            self.db.similarity_search(
                query,
                k=k
            )
        )