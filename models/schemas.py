from typing import Optional
from pydantic import BaseModel


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
    address_1: str
    address_2: Optional[str] = None
    city: str
    state: str
    zip: int
    country: str

    class Config:
        from_attributes = True


class AddressByCity(BaseModel):
    country: str

    class Config:
        from_attributes = True
