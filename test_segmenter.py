# test_segmenter.py

from src.ingestion.pdf_processor import PDFProcessor
from src.ingestion.smart_segmenter import SmartSegmenter

text = PDFProcessor().extract_text(
    "uploads/Medical_Narratives_3.pdf"
)

segments = SmartSegmenter().split(text)

print("TOTAL SEGMENTS:", len(segments))

for i, seg in enumerate(segments):
    print("\n--- SEGMENT", i+1, "---")
    print(seg[:200])