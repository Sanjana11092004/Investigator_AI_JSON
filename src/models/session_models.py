from pydantic import BaseModel


class SessionContext(BaseModel):

    session_id: str

    active_study_id: str | None = None

    active_patient_id: str | None = None

    active_document_id: str | None = None

    last_query: str | None = None