from pydantic import BaseModel


class TODO(BaseModel):
    content: str
    done: bool
