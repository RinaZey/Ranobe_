from pydantic import BaseModel

class RanobeObject(BaseModel):
    title: str | None = None
    creator: str | None = None

    status: str | None = None

    tags: list[int] | None = None
    genres: list[int] | None = None
