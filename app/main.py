from fastapi import FastAPI
from app.api.routes import product

app = FastAPI()

# Include the product routes
app.include_router(product.router, prefix="/api", tags=["products"])
