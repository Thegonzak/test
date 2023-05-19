from pydantic import BaseModel
from typing import Union

class Item(BaseModel):
    id: int
    name: Union[str, None]
    description: Union[str, None]
    stock: int
    price: float

class ItemRequest(BaseModel):
    name: Union[str, None]
    description: Union[str, None]
    stock: int
    price: float
    
class StockRequest(BaseModel):
    stock: int
    