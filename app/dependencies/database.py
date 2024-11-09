# app/dependencies/database.py
from app.config.db import db

# MongoDB collections
product_collection = db.get_collection("products")

# Dependency to access MongoDB collections
async def get_collection(collection_name: str):
    return db.get_collection(collection_name)
