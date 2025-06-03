from fastapi import FastAPI
from app.api.v1.endpoints import users, products, transactions, files

# This is the main entry point for the FastAPI application.
# It initializes the FastAPI app and includes the routers for different endpoints.
app = FastAPI(title="Inventory Tacker API", version="1.0.0")

# Include the routers for different endpoints
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(products.router, prefix="/api/v1/products", tags=["products"])
app.include_router(transactions.router, prefix="/api/v1/transactions", tags=["transactions"])
app.include_router(files.router, prefix="/api/v1/files", tags=["files"])


