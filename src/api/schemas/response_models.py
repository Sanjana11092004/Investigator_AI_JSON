from pydantic import BaseModel
from typing import Any


class QueryResponse(BaseModel):

    answer: dict


class HealthResponse(BaseModel):

    status: str
    

class ChatResponse(BaseModel):

    response: Any