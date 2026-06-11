from pydantic import BaseModel
from typing import Optional


class TagBase(BaseModel):
    name: str
    color: Optional[str] = None
    description: Optional[str] = None


class TagCreate(TagBase):
    pass


class TagUpdate(BaseModel):
    name: Optional[str] = None
    color: Optional[str] = None
    description: Optional[str] = None


class TagRead(TagBase):
    id: int

    model_config = {
        "from_attributes": True
    }
