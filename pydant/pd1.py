from pydantic import BaseModel, ValidationError, validator, Field
from typing import List, Dict


from pydantic import BaseModel, Field
from typing import List


class User(BaseModel):
    username: str
    email: str
    age: int = Field(..., gt=0)  # age must be greater than 0
    tags: List[str] = []


# Creating an instance
user_data = {
    "username": "john_doe",
    "email": "john.doe@example.com",
    "age": 25,
    "tags": ["admin", "editor"],
}

user = User(**user_data)

print(user)
