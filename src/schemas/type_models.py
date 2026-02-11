import uuid

from datetime import datetime

from pydantic import BaseModel, Field


class SourceDocument(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    filename: str
    uploaded_at: datetime
    page_count: int | None = None
    last_page: int | None = None


class TextChunk(BaseModel):
    id: int
    document_id: uuid.UUID
    text: str
    page_number: int
    embedding: list[float]
