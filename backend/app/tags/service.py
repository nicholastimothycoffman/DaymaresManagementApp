# app/tags/service.py

from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.tags.models import Tag
from app.tags.schemas import TagCreate, TagUpdate


def create_tag(db: Session, tag: TagCreate):
    normalized_name = tag.name.strip().lower()
    existing = db.query(Tag).filter(
    Tag.name == normalized_name
    ).first()

    if existing:
        raise HTTPException(
	    status_code=400, 
	    detail="Tag already exists"
	)

    db_tag = Tag(
	name=normalized_name,
	color=tag.color,
	description=tag.description,
    )
    
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    
    return db_tag


def get_tags(db: Session):
    return db.query(Tag).order_by(Tag.name).all()


def get_tag(db: Session, tag_id: int):
    tag = db.query(Tag).filter(Tag.id == tag_id).first()
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    return tag


def update_tag(db: Session, tag_id: int, tag_update: TagUpdate):
    tag = get_tag(db, tag_id)

    for field, value in tag_update.model_dump(exclude_unset=True).items():
        setattr(tag, field, value)

    db.commit()
    db.refresh(tag)
    return tag


def delete_tag(db: Session, tag_id: int):
    tag = get_tag(db, tag_id)
    db.delete(tag)
    db.commit()
    return {"message": "Tag deleted"}
