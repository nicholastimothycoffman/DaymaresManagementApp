from sqlalchemy import (
    Column,
    Integer,
    String,
    Table,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from app.core.database import Base


entity_tags = Table(
    "entity_tags",
    Base.metadata,
    Column(
        "entity_id",
        Integer,
        ForeignKey("entities.id"),
        primary_key=True,
    ),
    Column(
        "tag_id",
        Integer,
        ForeignKey("tags.id"),
        primary_key=True,
    ),
)


class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(
        String,
        unique=True,
        nullable=False,
        index=True,
    )

    color = Column(String, nullable=True)

    description = Column(String, nullable=True)

    entities = relationship(
        "Entity",
        secondary=entity_tags,
        back_populates="tags",
    )
