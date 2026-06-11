from fastapi import FastAPI

from app.core.database import Base, engine
from app.entities.routes import router as entities_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Daymares Management App")

app.include_router(
    entities_router,
    prefix="/entities",
    tags=["entities"],
)


@app.get("/")
def root():
    return {"message": "Daymares Management App API"}
