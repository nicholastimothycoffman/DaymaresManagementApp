# app/tags/routes.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.tags.schemas import TagCreate, TagUpdate, TagRead
from app.tags import service

router = APIRouter(prefix="/tags", tags=["tags"])


@router.post("/", response_model=TagRead)
def create_tag(tag: TagCreate, db: Session = Depends(get_db)):
    return service.create_tag(db, tag)


@router.get("/", response_model=list[TagRead])
def list_tags(db: Session = Depends(get_db)):
    return service.get_tags(db)


@router.get("/{tag_id}", response_model=TagRead)
def get_tag(tag_id: int, db: Session = Depends(get_db)):
    return service.get_tag(db, tag_id)


@router.patch("/{tag_id}", response_model=TagRead)
def update_tag(tag_id: int, tag_update: TagUpdate, db: Session = Depends(get_db)):
    return service.update_tag(db, tag_id, tag_update)


@router.delete("/{tag_id}")
def delete_tag(tag_id: int, db: Session = Depends(get_db)):
    return service.delete_tag(db, tag_id)
