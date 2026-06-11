from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class EntityBase(BaseModel):
    name: str
    entity_type: str

    email: Optional[str] = None
    phone: Optional[str] = None
    website: Optional[str] = None

    city: Optional[str] = None
    region: Optional[str] = None
    country: Optional[str] = None

    notes: Optional[str] = None


class EntityCreate(EntityBase):
    pass


class EntityUpdate(BaseModel):
    name: Optional[str] = None
    entity_type: Optional[str] = None

    email: Optional[str] = None
    phone: Optional[str] = None
    website: Optional[str] = None

    city: Optional[str] = None
    region: Optional[str] = None
    country: Optional[str] = None

    notes: Optional[str] = None


class EntityRead(EntityBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
