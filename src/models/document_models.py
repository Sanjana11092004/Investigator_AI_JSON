from datetime import datetime
from typing import Any
from typing import Dict
from uuid import uuid4

from pydantic import BaseModel
from pydantic import Field


class ClinicalDocument(BaseModel):

    document_id: str = Field(
        default_factory=lambda: str(uuid4())
    )

    file_name: str | None = None
    
    version: int = 1

    source_file: str

    source_type: str

    category: str

    ingested_at: datetime = Field(
        default_factory=datetime.utcnow
    )

    metadata: Dict[str, Any] = Field(
        default_factory=dict
    )

    data: Dict[str, Any] = Field(
        default_factory=dict
    )