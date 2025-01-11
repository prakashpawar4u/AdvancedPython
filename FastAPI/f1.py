from fastapi import FastAPI, Query, Body
from pydantic import BaseModel
from fastapi.testclient import TestClient

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None
    # description: str = None


@app.post("/items/")
async def create_item(item: Item):
    return item


@app.get("/items/")
async def read_items(q: str = Query(None, max_length=50)):
    return {"q": q}


# Create a TestClient using the FastAPI app
client = TestClient(app)

# # Test the POST /items/ endpoint
# response = client.post(
#     "/items/",
#     json={
#         "name": "Test Item",
#         "price": 10.5,
#         "is_offer": True,
#         # "description": "This is a test item",
#     },
# )

response = client.post(
    "/items/", json={"name": "Test Item", "price": 10.5, "is_offer": True}
)
assert response.status_code == 200, response.text
print(response.json())
print(response.status_code)
assert response.json() == {"name": "Test Item", "price": 10.5, "is_offer": True}

# Test the GET /items/ endpoint with a valid query parameter
response = client.get("/items/", params={"q": "test_query"})
assert response.status_code == 200, response.text
assert response.json() == {"q": "test_query"}

# Test the GET /items/ endpoint with an invalid query parameter (too long)
response = client.get("/items/", params={"q": "a" * 51})
assert response.status_code == 422, response.text

print("All tests passed successfully.")
