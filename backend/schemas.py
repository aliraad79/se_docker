from pydantic import BaseModel
from typing import Union


class ItemBase(BaseModel):
    name: str
    price: str


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True
