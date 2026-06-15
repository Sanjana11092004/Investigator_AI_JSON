from src.ingestion.pdf_processor import (
    PDFProcessor
)

from src.vector.chunking_service import (
    ChunkingService
)

print("STEP 1")

pdf = PDFProcessor()

print("STEP 2")

text = pdf.extract_text(
    "uploads/Medical_Narratives_2.pdf"
)

print(
    "TEXT LENGTH:",
    len(text)
)

chunker = ChunkingService()

print("STEP 3")

chunks = chunker.chunk_text(
    text
)

print(
    "TOTAL CHUNKS:",
    len(chunks)
)

for i, chunk in enumerate(
    chunks[:3]
):

    print(
        f"\n--- CHUNK {i+1} ---"
    )

    print(
        chunk[:300]
    )