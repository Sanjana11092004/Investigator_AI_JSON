from src.ingestion.pdf_processor import (
    PDFProcessor
)

pdf = PDFProcessor()

text = pdf.extract_text(
    "uploads/Medical_Narratives.pdf"
)

print(
    "Characters:",
    len(text)
)

print(
    "Words:",
    len(text.split())
)

print(
    text[:1000]
)