from fastapi import APIRouter
from app.models.customer import Customer
from app.services.customer_service import get_all_customers, get_customer, create_customer
from fastapi import APIRouter, status

router = APIRouter(prefix="/customers", tags=["customers"])

@router.get("/")
def read_customers():
    return get_all_customers()

@router.get("/{customer_id}")
def read_customer(customer_id: int):
    return get_customer(customer_id)

@router.post("/", status_code=status.HTTP_201_CREATED)
def add_customer(customer: Customer):
    return create_customer(customer)
