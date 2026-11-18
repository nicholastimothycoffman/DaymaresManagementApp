from fastapi import HTTPException
from sqlalchemy import delete, insert, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session, selectinload

from app.entities.models import Entity
from app.entities.schemas import EntityCreate, EntityUpdate
from app.tags.models import entity_tags
from app.tags.service import get_tag


def get_entities(db: Session, tag_id: int | None = None):
    query = select(Entity).options(selectinload(Entity.tags))
    if tag_id is not None:
        query = query.where(Entity.tags.any(id=tag_id))
    return db.scalars(query.order_by(Entity.name, Entity.id)).all()


def get_entity(db: Session, entity_id: int):
    return db.query(Entity).filter(Entity.id == entity_id).first()


def create_entity(db: Session, entity_data: EntityCreate):
    entity = Entity(**entity_data.model_dump())
    db.add(entity)
    db.commit()
    db.refresh(entity)
    return entity


def update_entity(db: Session, entity_id: int, entity_data: EntityUpdate):
    entity = get_entity(db, entity_id)

    if entity is None:
        return None

    update_data = entity_data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(entity, field, value)

    db.commit()
    db.refresh(entity)
    return entity


def delete_entity(db: Session, entity_id: int):
    entity = get_entity(db, entity_id)

    if entity is None:
        return None

    db.delete(entity)
    db.commit()
    return entity


def set_entity_tag(db: Session, entity_id: int, tag_id: int, *, assigned: bool):
    entity = get_entity(db, entity_id)
    if entity is None:
        raise HTTPException(status_code=404, detail="Entity not found")
    get_tag(db, tag_id)

    matching_link = (
        (entity_tags.c.entity_id == entity_id) & (entity_tags.c.tag_id == tag_id)
    )
    if assigned:
        try:
            db.execute(insert(entity_tags).values(entity_id=entity_id, tag_id=tag_id))
            db.commit()
        except IntegrityError:
            db.rollback()
            if not db.scalar(select(1).select_from(entity_tags).where(matching_link)):
                raise
    else:
        db.execute(delete(entity_tags).where(matching_link))
        db.commit()

    db.refresh(entity, attribute_names=["tags"])
    return entity
