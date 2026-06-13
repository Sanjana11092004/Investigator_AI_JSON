from pydantic import BaseModel


class QueryRequest(BaseModel):

    question: str

    session_id: str


class SessionRequest(BaseModel):

    session_id: str


class ChatRequest(BaseModel):

    session_id: str

    question: str