from fastapi import FastAPI
from router import customers, categories, operations, transactions
from db import *
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(application: FastAPI):
    init_db()
    get_session()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(customers.customerRouter)
app.include_router(categories.categoryRouter)
app.include_router(operations.operationRouter)
app.include_router(transactions.transactionRouter)

