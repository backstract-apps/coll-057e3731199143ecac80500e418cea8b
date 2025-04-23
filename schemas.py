from pydantic import BaseModel

import datetime

import uuid

from typing import Any, Dict, List, Tuple

class Persons(BaseModel):
    rollnumber: int
    fullname: str
    age: int
    profession: str


class ReadPersons(BaseModel):
    rollnumber: int
    fullname: str
    age: int
    profession: str
    class Config:
        from_attributes = True


class Addresses(BaseModel):
    id: int
    street: str
    city: str
    state: str
    country: str
    postal_code: str
    created_at: datetime.time
    updated_at: datetime.time


class ReadAddresses(BaseModel):
    id: int
    street: str
    city: str
    state: str
    country: str
    postal_code: str
    created_at: datetime.time
    updated_at: datetime.time
    class Config:
        from_attributes = True




class PutPersonsRollnumber(BaseModel):
    rollnumber: str
    fullname: str
    age: str
    profession: str

    class Config:
        from_attributes = True



class PostAddresses(BaseModel):
    city: str
    state: str
    country: str
    postal_code: str
    created_at: str
    updated_at: str

    class Config:
        from_attributes = True



class PutAddressesId(BaseModel):
    id: str
    street: str
    city: str
    state: str
    country: str
    postal_code: str
    created_at: str
    updated_at: str

    class Config:
        from_attributes = True

