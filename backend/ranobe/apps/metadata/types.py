from pydantic import BaseModel

class TagObject(BaseModel):
    id: int | None = None
    name: str | None = None

class GenreObject(BaseModel):
    id: int | None = None
    name: str | None = None
