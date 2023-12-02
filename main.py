from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel

app = FastAPI()

class Product(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def test_api():
    return {"message": "Hello world"}

@app.get("/product/{product_name}")
def get_product_name(product_name: str, q = None):
    return {"product": product_name, "q": q}

@app.put("/product/{product_id}")
def update_item(product_id: int, product: Product):
    return {"item_name": product.name, "item_id": product_id}