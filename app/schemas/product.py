# app/schemas/product.py
from pydantic import BaseModel
from typing import Optional

class ProductSchema(BaseModel):
    id: Optional[str]  # MongoDB's ObjectId is a string
    name: str
    image: str
    price: float
    offer: Optional[float] = None
    hide_price: bool = False
    add_to_cart: bool = False
    category: str

    class Config:
        orm_mode = True
