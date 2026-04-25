from pydantic import BaseModel


class Address(BaseModel):
    city: str
    zip_code: str


class User(BaseModel):
    id: int
    name: str
    address: Address


user = User(id=1,
            name="Alice",
            address=Address(city="New York", zip_code="555"))

print(user.model_dump_json())
