from typing import Any
from typing import Dict

from pydantic import BaseModel


class QueryRequest(BaseModel):

    question: str

    session_id: str


class QueryResponse(BaseModel):

    answer: str

    retrieved_data: Dict[str, Any]

    session_context: Dict[str, Any]