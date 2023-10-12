from dataclasses import dataclass


@dataclass
class Order:
    order_id: str
    item_id: str
    price: int
