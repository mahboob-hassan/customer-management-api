from pydantic import BaseModel
from typing import List

class CustomerCreate(BaseModel):        
    name: str
    email: str
    city: str

class Customer(BaseModel):
    id : int
    name: str
    email: str
    city: str


class CustomerListResponse(BaseModel):
    results : List[Customer]