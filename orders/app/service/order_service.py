from fastapi import Depends
from app.repository.order_repository import OrderRepository


class OrderService:

    def __init__(self, repo = Depends(OrderRepository)) -> None:
        self.repo = repo

    def get_order(self, order_id):
        return self.repo.get_order(order_id)
    
    def get_orders(self):
        return self.repo.get_orders()
    
    def create_order(self, item_id, price):
        return self.repo.create_order(item_id, price)