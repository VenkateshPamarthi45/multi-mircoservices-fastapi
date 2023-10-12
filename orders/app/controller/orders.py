from fastapi import Depends, FastAPI, APIRouter
from app.models.request import OrderRequest

from app.service.order_service import OrderService

router = APIRouter()

@router.get("/{order_id}")
def get_order(order_id, service= Depends(OrderService)):
    print({order_id})
    return service.get_order(order_id)

@router.get("")
def get_orders(service= Depends(OrderService)):
    return service.get_orders()

@router.post("")
def create_orders(request:OrderRequest, service= Depends(OrderService)):
    return service.create_order(request.item_id,request.price)

