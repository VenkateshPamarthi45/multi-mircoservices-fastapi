from fastapi import FastAPI

from app.controller import orders

app = FastAPI()

app.include_router(orders.router,prefix="/v1/orders")

@app.get("/index")
def index():
    return {"msg":"welcome orders api"}