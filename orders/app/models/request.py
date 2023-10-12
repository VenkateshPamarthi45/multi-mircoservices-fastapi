from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class OrderRequest(BaseModel):
    item_id:str
    price:int