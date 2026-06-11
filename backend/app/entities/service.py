from sqlalchemy.orm import Session

from app.entities.models import Entity
from app.entities.schemas import EntityCreate, EntityUpdate


def get_entities(db: Session):
    return db.query(Entity).order_by(Entity.name.asc()).all()


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
