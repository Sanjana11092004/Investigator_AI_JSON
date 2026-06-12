from pydantic import BaseModel


class QueryResponse(BaseModel):

    answer: dict


class HealthResponse(BaseModel):

    status: str