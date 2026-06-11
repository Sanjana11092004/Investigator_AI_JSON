from src.models.document_models import ClinicalDocument
from src.models.session_models import SessionContext
from src.models.query_models import QueryRequest


doc = ClinicalDocument(
    source_file="study001.pdf",
    source_type="pdf",
    category="study",
)

session = SessionContext(
    session_id="abc123"
)

query = QueryRequest(
    question="Show labs for SUBJ-0001",
    session_id="abc123"
)

print(doc.model_dump())

print(session.model_dump())

print(query.model_dump())