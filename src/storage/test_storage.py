from src.models.document_models import ClinicalDocument

from src.storage.json_store import JSONStore
from src.storage.metadata_store import MetadataStore


document = ClinicalDocument(

    source_file="sample.pdf",

    source_type="pdf",

    category="studies",

    metadata={
        "study_id": "NCT001"
    },

    data={
        "sponsor": "Pfizer"
    }
)

json_store = JSONStore()

metadata_store = MetadataStore()

path = json_store.save_document(
    document
)

metadata_store.register_document(
    document_id=document.document_id,
    category=document.category,
    source_file=document.source_file,
    source_type=document.source_type,
    json_path=str(path)
)

print("Saved JSON:")
print(path)

loaded = json_store.load_document(
    path
)

print("\nLoaded JSON:")
print(loaded)