from src.ingestion.pdf_processor import (
    PDFProcessor
)

from src.vector.chunking_service import (
    ChunkingService
)

from src.vector.vector_store import (
    VectorStore
)

print("STEP 1")

text = (
    PDFProcessor()
    .extract_text(
        "uploads/Medical_Narratives_2.pdf"
    )
)

print("STEP 2")

chunks = (
    ChunkingService()
    .chunk_text(text)
)

print(
    f"CHUNKS: {len(chunks)}"
)

metadata = []

for i in range(
    len(chunks)
):

    metadata.append(

        {
            "source":
            "Medical_Narratives_2.pdf",

            "chunk_id":
            str(i)
        }

    )

print("STEP 3")

store = VectorStore()

print("STEP 4")

store.add_chunks(
    chunks,
    metadata
)

print(
    "SUCCESSFULLY STORED"
)