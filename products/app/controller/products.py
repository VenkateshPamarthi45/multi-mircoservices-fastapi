from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from starlette import status
from starlette.exceptions import HTTPException
from starlette.responses import JSONResponse
from app.handlers.custom_exceptions import ProductNotFoundException
from app.models.requests import ProductRequest

from app.service.product_service import ProductService


router = APIRouter()


@router.get("/{product_id}")
def get_product(product_id: str, handler=Depends(ProductService)):
    product = handler.get_product_detail(product_id)
    if isinstance(product, str):
        raise ProductNotFoundException()
    else:
        return JSONResponse(
            status_code=status.HTTP_200_OK, content=jsonable_encoder(product)
        )


@router.post("")
def create_product(product: ProductRequest, handler=Depends(ProductService)):
    product = handler.new_product(product)
    if isinstance(product, str):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=product)
    else:
        return JSONResponse(
            status_code=status.HTTP_200_OK, content=jsonable_encoder(product)
        )
