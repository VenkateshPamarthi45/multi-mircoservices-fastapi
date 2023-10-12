from app.data.order import Order


class OrderRepository:
    orders = {}

    def __init__(self) -> None:
        pass
    
    def get_orders(self):
        return self.orders

    def get_order(self, order_id):
        if str(order_id) in self.orders:
            return self.orders[order_id]
        else:
            return "No Order found"
        
    def create_order(self, item_id:str, price:int):
        new_order_id = str(len(self.orders.keys()) + 1)
        order = Order(
            order_id=new_order_id, item_id=item_id, price=price
        )
        self.orders[new_order_id] = order
        return order