from pydantic import BaseModel
from typing import Optional

class ProductCreate(BaseModel):
    name: str
    image: str
    price: float
    offer: Optional[float] = None
    hide_price: bool = False
    add_to_cart: bool = False
    category: str

class ProductResponse(ProductCreate):
    id: str
