from typing import List

from fastapi import APIRouter, Depends, HTTPException
from db import get_session
from models.models import Customer, CustomerCategory

customerRouter = APIRouter(prefix="/customers", tags=["Пользователь"])  # tags отвечает за swagger


@customerRouter.get("/", response_model=list[CustomerCategory])
async def get_customers(session=Depends(get_session)) -> List[Customer]:
    customers = session.query(Customer).all()
    return customers


@customerRouter.get("/{username_id}", response_model=CustomerCategory)
async def get_customer(username_id: int, session=Depends(get_session)) -> Customer:
    customer = session.get(Customer, username_id)
    return customer


@customerRouter.post("/")
async def create_customer(customer: Customer, session=Depends(get_session)):
    customer.id = None
    session.add(customer)
    session.commit()
    session.refresh(customer)
    return customer


@customerRouter.patch("/{username_id}")
async def update_customer(customer: Customer, username_id: int, session=Depends(get_session)):
    customer_from_db = session.query(Customer).filter_by(id=username_id).first()
    if customer_from_db is None:  # если запись с переданным id не найдена, то возвращаем исключение
        raise HTTPException(status_code=404, detail="No such customer")
    customer_data = customer.model_dump(exclude_unset=True)
    for key, value in customer_data.items():
        if value is None:
            continue
        setattr(customer_from_db, key, value)
    session.add(customer_from_db)
    session.commit()
    session.refresh(customer_from_db)
    return customer_from_db


@customerRouter.delete("/{username_id}")
async def delete_customer(username_id: int, session=Depends(get_session)):
    session.query(Customer).filter_by(id=username_id).delete()
    session.commit()
    return "Deleted"
