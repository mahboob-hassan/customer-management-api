from fastapi import FastAPI
from app.routers import customers

app = FastAPI(title="Customer Management API")

app.include_router(customers.router)

@app.get('/')
def read_root():
    return {"message": "Customer API is running"}
