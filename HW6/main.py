from fastapi import FastAPI, HTTPException
from models import Product, Order, User
from crud import create_product, read_product
from database import database, init_db
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()

init_db()


@app.post("/products/", response_model=Product)
async def create_product_route(product: Product):
    created_product = await create_product(database, product)
    return JSONResponse(content=created_product, status_code=201)

@app.get("/products/{product_id}", response_model=Product)
async def read_product_route(product_id: int):
    product = await read_product(database, product_id)
    if product:
        return product
    raise HTTPException(status_code=404, detail="Product not found")

# Implement similar routes for other CRUD operations

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
