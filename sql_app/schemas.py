# Estos esquemas estan realcionados con los modelos
# 

from typing import Union
from pydantic import BaseModel

class ItemBase(BaseModel):
    title: str
    description: Union[str, None] = None

class ItemCreate(ItemBase):
    pass

# Estos esquemas (models de pydantic) se van
# utilizar para leer datos, al devolverlos de la API.
class Item(ItemBase):
    id:int
    owner_id:int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    items : list[Item] = []

    class Config:
        orm_mode = True
