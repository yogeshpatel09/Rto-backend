from fastapi import FastAPI
from app.api.routes.product import router as product_router

app = FastAPI(debug=True)  # Enable debug mode for more detailed error output

# Include the product routes
app.include_router(product_router, prefix="/products", tags=["products"])
