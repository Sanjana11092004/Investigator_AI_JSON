from src.ingestion.pdf_processor import (
    PDFProcessor
)

from src.ingestion.narrative_splitter import (
    NarrativeSplitter
)


pdf = PDFProcessor()

text = pdf.extract_text(
    "uploads/Medical_Narratives.pdf"
)

splitter = (
    NarrativeSplitter()
)

narratives = (
    splitter.split(text)
)

print(
    "Narratives:",
    len(narratives)
)

print("\nFIRST NARRATIVE\n")

print(
    narratives[0][:1000]
)