from sqlalchemy.orm import Session

from . import models, schemas


def create_item(db: Session, item: schemas.ItemBase):
    item = models.Item(name=item.name, price=item.price)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def get_items_with_id(db: Session, id: int):
    return db.query(models.Item).filter(models.Item.id == id).first()


def update_item(db: Session, item: models.Item, item_id: int):
    db.query(models.Item).filter(models.Item.id == item_id).update(
        {"name": item.name, "price": item.price}
    )
    db.commit()


def delete_item(db: Session, item_id: int):
    db.query(models.Item).filter(models.Item.id == item_id).delete()
    db.commit()
