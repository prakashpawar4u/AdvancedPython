# from pydantic import BaseModel, ValidationError


# class Person(BaseModel):
#     name: str
#     age: int
#     email: str


# # create object of Person
# try:
#     # This will raise an error because age should be an integer, not a string
#     person = Person(name="John Doe", age="3jf0", email="johndoe@example.com")
#     print(person)
# except ValidationError as e:
#     print(e)


# Example 3: Using Default Values and Optional Fields
# Pydantic models can also include optional fields and default values.

# from pydantic import BaseModel
# from typing import Optional


# class Person(BaseModel):
#     name: str
#     age: Optional[int] = None  # This is an optional field with a default value of None
#     email: str
#     phone: Optional[str] = None  # Optional phone number


# # Create an instance of Person without age and phone
# person = Person(name="Alice", email="alice@example.com")

# print(person)


# Example 4: Parsing JSON Data with Pydantic
# Pydantic can easily handle parsing and validating data coming from JSON.

# from pydantic import BaseModel
# import json


# class Person(BaseModel):
#     name: str
#     age: int
#     email: str


# # Sample JSON data
# data = '{"name": "Bob", "age": 25, "email": "bob@example.com"}'

# # Parse the JSON data into a Pydantic model
# person = Person.parse_raw(data)

# print(person)


from pydantic import BaseModel, ValidationError, validator
from typing import List, Dict


class Item(BaseModel):
    name: str
    price: float
    tags: List[str]

    @validator("price")
    def check_price_positive(cls, value):
        if value <= 0:
            raise ValueError("price must be positive")
        return value


try:
    item = Item(name="Laptop", price=-1000, tags=["electronics", "computer"])
except ValueError as e:
    print(e)
