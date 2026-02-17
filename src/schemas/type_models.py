import uuid

from pathlib import Path

from pydantic import BaseModel, Field


class SourceDocument(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    filename: str
    filepath: Path
    page_count: int | None = None
    start_page: int | None = None
    end_page: int | None = None


class TextChunk(BaseModel):
    id: int
    document_id: uuid.UUID
    text: str
    page_number: int
    embedding: list[float]
