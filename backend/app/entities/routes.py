from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.entities import service
from app.entities.schemas import EntityCreate, EntityRead, EntityUpdate

router = APIRouter()


@router.get("/", response_model=List[EntityRead])
def list_entities(db: Session = Depends(get_db)):
    return service.get_entities(db)


@router.get("/{entity_id}", response_model=EntityRead)
def read_entity(entity_id: int, db: Session = Depends(get_db)):
    entity = service.get_entity(db, entity_id)

    if entity is None:
        raise HTTPException(status_code=404, detail="Entity not found")

    return entity


@router.post("/", response_model=EntityRead, status_code=201)
def create_entity(entity_data: EntityCreate, db: Session = Depends(get_db)):
    return service.create_entity(db, entity_data)


@router.put("/{entity_id}", response_model=EntityRead)
def update_entity(
    entity_id: int,
    entity_data: EntityUpdate,
    db: Session = Depends(get_db),
):
    entity = service.update_entity(db, entity_id, entity_data)

    if entity is None:
        raise HTTPException(status_code=404, detail="Entity not found")

    return entity


@router.delete("/{entity_id}", response_model=EntityRead)
def delete_entity(entity_id: int, db: Session = Depends(get_db)):
    entity = service.delete_entity(db, entity_id)

    if entity is None:
        raise HTTPException(status_code=404, detail="Entity not found")

    return entity
