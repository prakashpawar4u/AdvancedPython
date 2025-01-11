import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


# Define a Pydantic model for request payload validation
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None


# In-memory storage for items
items = {}


# Endpoint to create an item
@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    items[item.name] = item.dict()
    logger.info("Item created: %s", item.dict())
    return item


# Endpoint to read an item by name
@app.get("/items/{item_name}", response_model=Item)
async def read_item(item_name: str):
    item = items.get(item_name)
    if item:
        logger.info("Item retrieved: %s", item)
        return item
    logger.error("Item not found: %s", item_name)
    raise HTTPException(status_code=404, detail="Item not found")


# Endpoint to update an item
@app.put("/items/{item_name}", response_model=Item)
async def update_item(item_name: str, item: Item):
    if item_name in items:
        items[item_name] = item.dict()
        logger.info("Item updated: %s", item.dict())
        return item
    logger.error("Item not found for update: %s", item_name)
    raise HTTPException(status_code=404, detail="Item not found")


# Endpoint to delete an item
@app.delete("/items/{item_name}", response_model=dict)
async def delete_item(item_name: str):
    if item_name in items:
        del items[item_name]
        logger.info("Item deleted: %s", item_name)
        return {"message": "Item deleted successfully"}
    logger.error("Item not found for deletion: %s", item_name)
    raise HTTPException(status_code=404, detail="Item not found")


# Endpoint to get all items
@app.get("/items/", response_model=dict)
async def get_all_items():
    logger.info("All items retrieved")
    return items
