import requests
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BASE_URL = "http://127.0.0.1:8000"


# Function to create an item
def create_item(name, price, is_offer):
    response = requests.post(
        f"{BASE_URL}/items/", json={"name": name, "price": price, "is_offer": is_offer}
    )
    if response.status_code == 200:
        logger.info("Item created successfully: %s", response.json())
    else:
        logger.error("Failed to create item: %s", response.text)


# Function to read an item by name
def read_item(item_name):
    response = requests.get(f"{BASE_URL}/items/{item_name}")
    if response.status_code == 200:
        logger.info("Item retrieved successfully: %s", response.json())
    else:
        logger.error("Failed to retrieve item: %s", response.text)


# Function to update an item
def update_item(item_name):
    response = requests.put(
        f"{BASE_URL}/items/{item_name}",
        json={"name": "apple", "price": 2.2, "is_offer": False},
    )
    if response.status_code == 200:
        logger.info("Item updated successfully: %s", response.json())
    else:
        logger.error("Failed to update item: %s", response.text)


# Function to delete an item
def delete_item(item_name):
    response = requests.delete(f"{BASE_URL}/items/{item_name}")
    if response.status_code == 200:
        logger.info("Item deleted successfully: %s", response.json())
    else:
        logger.error("Failed to delete item: %s", response.text)


# Function to get all items
def get_all_items():
    response = requests.get(f"{BASE_URL}/items/")
    if response.status_code == 200:
        logger.info("All items retrieved successfully: %s", response.json())
    else:
        logger.error("Failed to retrieve items: %s", response.text)


# Test the functions
create_item("apple", 1.2, False)
create_item("banana", 0.5, True)
get_all_items()
read_item("apple")
update_item("apple")
delete_item("banana")
delete_item("apple")
