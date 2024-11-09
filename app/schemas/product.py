from pydantic import BaseModel
from typing import Optional

class ProductSchema(BaseModel):
    id: Optional[str]  # Change id type to str to match MongoDB's ObjectId
    name: str
    image: str
    price: float
    offer: Optional[float] = None
    hide_price: bool = False
    add_to_cart: bool = False
    category: str

    class Config:
        orm_mode = True
