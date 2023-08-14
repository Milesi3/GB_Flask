from sqlalchemy import select
from databases import Database
from models import ProductModel, OrderModel, UserModel, Product, Order, User

async def create_product(database: Database, product: Product):
    query = ProductModel.insert().values(**product.dict())
    product_id = await database.execute(query)
    return {**product.dict(), "id": product_id}

async def read_product(database: Database, product_id: int):
    query = select(ProductModel).where(ProductModel.c.id == product_id)
    product = await database.fetch_one(query)
    if product:
        return product
    return None


