# app/crud/product.py
from app.dependencies.database import product_collection
from app.schemas.product import ProductSchema
from bson import ObjectId
from typing import List, Optional

# Helper function to convert MongoDB's ObjectId to string
def str_id(obj):
    return str(obj) if obj else None

async def create_product(product: ProductSchema):
    result = await product_collection.insert_one(product.dict())
    return {**product.dict(), "id": str(result.inserted_id)}

async def get_product_by_id(product_id: str):
    product = await product_collection.find_one({"_id": ObjectId(product_id)})
    if product:
        return {**product, "id": str(product["_id"])}
    return None

async def get_all_products(skip: int = 0, limit: int = 10) -> List[ProductSchema]:
    products = await product_collection.find().skip(skip).limit(limit).to_list(length=limit)
    return [{**product, "id": str(product["_id"])} for product in products]

async def update_product(product_id: str, product: ProductSchema):
    result = await product_collection.update_one(
        {"_id": ObjectId(product_id)},
        {"$set": product.dict()}
    )
    return result.modified_count > 0

async def delete_product(product_id: str):
    result = await product_collection.delete_one({"_id": ObjectId(product_id)})
    return result.deleted_count > 0
