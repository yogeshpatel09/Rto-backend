from fastapi import APIRouter, HTTPException
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductResponse
from app.config.db import db

router = APIRouter()

# Create a new product
@router.post("/products/", response_model=ProductResponse)
async def create_product(product: ProductCreate):
    product_data = product.dict()
    result = await db.products.insert_one(product_data)
    product_data["id"] = str(result.inserted_id)
    return ProductResponse(**product_data)

# Get all products
@router.get("/products/", response_model=list[ProductResponse])
async def get_products():
    products = []
    async for product in db.products.find():
        product["id"] = str(product["_id"])
        products.append(ProductResponse(**product))
    return products

# Get a product by ID
@router.get("/products/{product_id}", response_model=ProductResponse)
async def get_product(product_id: str):
    product = await db.products.find_one({"_id": product_id})
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    product["id"] = str(product["_id"])
    return ProductResponse(**product)
