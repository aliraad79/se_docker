from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/{item_id}")
def read_item(item_id: int, db: Session = Depends(get_db)):
    return crud.get_items_with_id(db, item_id)


@app.post("/")
def add_item(item: schemas.ItemBase, db: Session = Depends(get_db)):
    return crud.create_item(db, item)


@app.put("/{item_id}")
def update_item(item_id: int, item: schemas.ItemBase, db: Session = Depends(get_db)):
    crud.update_item(db, item, item_id) 
    return item


@app.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    crud.delete_item(db, item_id)
    return {"Result": "Ok"}
