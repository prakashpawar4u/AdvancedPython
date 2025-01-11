from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel

from fastapi.testclient import TestClient


app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None


@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    return item


@app.get("/items/{item_name}", response_model=Item)
async def read_item(item_name: str):
    items = {
        "apple": {"name": "apple", "price": 1.5, "is_offer": True},
        "banana": {"name": "banana", "price": 0.5, "is_offer": False},
    }
    item = items.get(item_name)

    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.put("/items/{item_name}", response_model=Item)
async def update_item(item_name: str, item: Item):
    items = {
        "apple": {"name": "apple", "price": 1.5, "is_offer": True},
        "banana": {"name": "banana", "price": 0.5, "is_offer": False},
    }
    if item_name not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_name] = item
    return item


@app.delete("/items/{item_name}", response_model=dict)
async def delete_item(item_name: str):
    items = {
        "apple": {"name": "apple", "price": 1.5, "is_offer": True},
        "banana": {"name": "banana", "price": 0.5, "is_offer": False},
    }
    if item_name not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_name]
    return {"message": "Item deleted successfully"}


client = TestClient(app)

# Test the POST /items/ endpoint
data = {"name": "apple", "price": 1.5, "is_offer": True}
response = client.post("/items/", json=data)
assert response.status_code == 200, response.text
assert response.json() == data

# Test the GET /items/{item_name} endpoint with an existing item
response = client.get("/items/apple")
assert response.status_code == 200, response.json() == data
print(response.json())
print(response.status_code)
