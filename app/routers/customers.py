from fastapi import APIRouter, HTTPException, status
from app.models.customer import Customer
from app.services.customer_service import get_all_customers, get_customer, create_customer

router = APIRouter(prefix="/customers", tags=["customers"])

@router.get("/")
def read_customers():
    return get_all_customers()

@router.get("/{customer_id}")
def read_customer(customer_id: int):
    customer = get_customer(customer_id)
    if customer is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")
    return customer

@router.post("/", status_code=status.HTTP_201_CREATED)
def add_customer(customer: Customer):
    return create_customer(customer)
