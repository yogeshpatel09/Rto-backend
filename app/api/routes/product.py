from fastapi import APIRouter, HTTPException
from app.schemas.product import ProductSchema
from app.config.db import product_collection
from bson import ObjectId
from typing import List

router = APIRouter()

# Helper function to convert MongoDB's ObjectId to string
def str_id(obj):
    return str(obj) if isinstance(obj, ObjectId) else obj

# Test MongoDB connection
@router.get("/test-db")
async def test_db():
    try:
        # Attempt to insert and retrieve a test document
        result = await product_collection.insert_one({"test": "data"})
        await product_collection.delete_one({"_id": result.inserted_id})
        return {"status": "MongoDB connection successful"}
    except Exception as e:
        print(f"Error testing MongoDB connection: {e}")
        raise HTTPException(status_code=500, detail="Unable to connect to MongoDB")

# Add a new product
@router.post("/add_new_product", response_model=ProductSchema)
async def add_product(product: ProductSchema):
    try:
        result = await product_collection.insert_one(product.dict())
        return {**product.dict(), "id": str(result.inserted_id)}
    except Exception as e:
        print(f"Error adding product: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Get a product by its ID
@router.get("/get_product_by_id/{product_id}", response_model=ProductSchema)
async def read_product(product_id: str):
    try:
        product = await product_collection.find_one({"_id": ObjectId(product_id)})
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        return {**product, "id": str(product["_id"])}
    except Exception as e:
        print(f"Error reading product with ID {product_id}: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Get all products with pagination
@router.get("/get_all_product", response_model=List[ProductSchema])
async def read_products(skip: int = 0, limit: int = 10):
    try:
        products = await product_collection.find().skip(skip).limit(limit).to_list(length=limit)
        return [{**product, "id": str(product["_id"])} for product in products]
    except Exception as e:
        print(f"Error reading products: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Update a product by its ID
@router.put("/update_product/{product_id}", response_model=ProductSchema)
async def update_product_route(product_id: str, product: ProductSchema):
    try:
        result = await product_collection.update_one(
            {"_id": ObjectId(product_id)},
            {"$set": product.dict()}
        )
        if result.modified_count == 0:
            raise HTTPException(status_code=404, detail="Product not found")

        updated_product = await product_collection.find_one({"_id": ObjectId(product_id)})
        return {**updated_product, "id": str(updated_product["_id"])}
    except Exception as e:
        print(f"Error updating product with ID {product_id}: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Delete a product by its ID
@router.delete("/delete_product/{product_id}", response_model=dict)
async def delete_product_route(product_id: str):
    try:
        result = await product_collection.delete_one({"_id": ObjectId(product_id)})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Product not found")
        return {"status": "Product deleted successfully"}
    except Exception as e:
        print(f"Error deleting product with ID {product_id}: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
