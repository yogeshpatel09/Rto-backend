from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    id: Optional[str]  # Optional ID
    name: str           # Required field
    image: str          # Required field
    price: float        # Required field
    offer: Optional[float] = None  # Optional field
    hide_price: bool = False  # Default value
    add_to_cart: bool = False  # Default value
    category: str       # Required field

    class Config:
        orm_mode = True  # Ensure Pydantic can work with MongoDB models
