from app.data.customers import customers
from app.models.customer import CustomerCreate

def get_all_customers():
    return customers

def get_customer(customer_id: int):
    for customer in customers:
        if customer["id"] == customer_id:
            return customer
    return None

def create_customer(customer: CustomerCreate):
    new_id = len(customers) + 1
    new_customer = customer.model_dump()
    new_customer["id"] = new_id
    customers.append(new_customer)
    return new_customer
