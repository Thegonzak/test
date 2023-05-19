from swagger_server.utils.logging import log as logging
from swagger_server.repository.item_repository import ItemRepository
from swagger_server.models.item_model import Item

from pydantic import parse_obj_as
from typing import List

class ItemUseCase():

    def __init__(self):
        log = logging()
        self.item_repository = ItemRepository()
        self.log = log

    def save(self, request):
        response = None
        data = self.item_repository.create(request.dict())
        response = parse_obj_as(Item, data)
        return response
    
    def get_item(self, item_id):
        response = self.item_repository.get_by_id(item_id)
        item = None
        if response:
            item = parse_obj_as(Item, response[0])
        return item
    
       
    
    def update(self, request, item_id):
        response = self.item_repository.update(request.dict(), item_id)
        item = parse_obj_as(Item, response)
        return item

    
    def get_paginated(self, page, size, name):
        response = self.item_repository.get_paginated(page, size, name)
        items = parse_obj_as(List[Item], response)
        return items