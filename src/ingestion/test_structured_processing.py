from src.ingestion.structured_converter import (
    StructuredConverter
)

converter = StructuredConverter()

files = converter.process_excel(
    "incoming/SDTM_100patients.xlsx"
)

print("\nGenerated Files:\n")

for f in files:
    print(f)