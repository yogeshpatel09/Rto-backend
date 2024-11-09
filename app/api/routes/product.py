# app/api/routes/product.py
from fastapi import APIRouter, Depends, HTTPException
from app.schemas.product import ProductSchema
from app.crud.product import create_product, get_product_by_id, get_all_products, update_product, delete_product
from typing import List

router = APIRouter()

@router.post("/", response_model=ProductSchema)
async def add_product(product: ProductSchema):
    return await create_product(product)

@router.get("/{product_id}", response_model=ProductSchema)
async def read_product(product_id: str):
    product = await get_product_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.get("/", response_model=List[ProductSchema])
async def read_products(skip: int = 0, limit: int = 10):
    return await get_all_products(skip=skip, limit=limit)

@router.put("/{product_id}", response_model=ProductSchema)
async def update_product_route(product_id: str, product: ProductSchema):
    updated = await update_product(product_id, product)
    if not updated:
        raise HTTPException(status_code=404, detail="Product not found")
    return {**product.dict(), "id": product_id}

@router.delete("/{product_id}", response_model=dict)
async def delete_product_route(product_id: str):
    deleted = await delete_product(product_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"status": "Product deleted successfully"}
