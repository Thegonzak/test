from pydantic import BaseModel
from typing import Union, List
from swagger_server.models.item_model import Item

class ErrorResponse(BaseModel):
    error_code: int
    error_message: str

class MessageResponse(BaseModel):
    message: str

class APIResponse(BaseModel):
    success: bool
    data: Union[
        None,
        Item,
        List[Item],
        ErrorResponse,
        MessageResponse,
    ]
