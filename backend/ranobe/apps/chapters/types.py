from pydantic import BaseModel

class ChapterObject(BaseModel):
    title: str | None = None
    ranobe: str | None = None
    volume: int | None = None
    number: int | None = None
    text: str | None = None
