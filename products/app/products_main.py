from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.controller import products
from app.handlers.custom_exceptions import ProductNotFoundException

app = FastAPI()

app.include_router(products.router, prefix="/v1/products")

@app.get("/index")
def index():
    return {"msg":"welcome products api"}

@app.exception_handler(ProductNotFoundException)
def product_not_found_exception_handler(req: Request, ex: ProductNotFoundException):
    
    return JSONResponse(
        status_code=ex.status_code,
        content={"message": f"{ex.message}"}
    )
