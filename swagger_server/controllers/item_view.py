import connexion
from flask.views import MethodView
from timeit import default_timer
from flask import jsonify


from swagger_server.utils.logging import log as logging
from swagger_server.models.response_model import APIResponse, ErrorResponse, MessageResponse
from swagger_server.models.item_model import ItemRequest
from swagger_server.uses_cases.item_use_case import ItemUseCase

class ItemView(MethodView):

    def __init__(self):
        log = logging()
        self.log = log


    def save_item(self):
        try:
            start_time = default_timer()
            self.log.info("Funcion: %r - Paquete: %r - Mensaje: Inicio de transacción", "save_item", __name__)

            item_created = None

            if connexion.request.is_json:
                request = ItemRequest(**connexion.request.get_json())
                item_use_case = ItemUseCase()
                item_created = item_use_case.save(request=request)
                
            api_response = APIResponse(
                success=True,
                data=item_created,
                error_code=0,
                error_message="",
                message=""
            )
            response = api_response.dict()
            end_time = default_timer()
            
            self.log.info("Funcion: %r - Paquete: %r - Mensaje: Fin de transacción, procesada en: %r milisegundos", "save_item", __name__, round(end_time - start_time)* 1000)
            return jsonify(response)
        
        except Exception as err:
            end_time = default_timer()
            error_response = APIResponse(
                success=False,
                data=ErrorResponse(
                    error_code=1,
                    error_message=str(err)
                ),
                error_code=1,
                error_message=str(err),
                message=""
            )
            error = error_response.dict()
            return jsonify(error) 

    def get_item_by_id(self, item_id):
        try:
            start_time = default_timer()
            self.log.info("Funcion: %r - Paquete: %r - Mensaje: Inicio de transacción", "get_item_by_id", __name__)
            item_use_case = ItemUseCase()
            item = item_use_case.get_item(item_id)
            api_response = None
            if item:
                api_response = APIResponse(success=True, data=item)
            else:
                api_response = APIResponse(success=True, data=MessageResponse(
                    message="No se encontro informacion"
                ))
            response = api_response.dict()
            end_time = default_timer()
            self.log.info("Funcion: %r - Paquete: %r - Mensaje: Fin de transacción, procesada en: %r milisegundos", "get_item_by_i", __name__, round(end_time - start_time)* 1000)
            return jsonify(response)
        except Exception as err:
            end_time = default_timer()
            error_response = APIResponse(
                success=False,
                data=ErrorResponse(
                    error_code=1,
                    error_message=str(err)
                )
            )
            error = error_response.dict()
            return jsonify(error) 
        return None
    
    
    
    def item_paginated(self, page, size, name):
        try:
            start_time = default_timer()
            self.log.info("Funcion: %r - Paquete: %r - Mensaje: Inicio de transacción", "task_get_all", __name__)
            item_use_case = ItemUseCase()
            items = item_use_case.get_paginated(page, size, name)
            api_response = APIResponse(success=True, data=items)
            response = api_response.dict()
            end_time = default_timer()
            self.log.info("Funcion: %r - Paquete: %r - Mensaje: Fin de transacción, procesada en: %r milisegundos", "task_get_all", __name__, round(end_time - start_time)* 1000)
            return jsonify(response)
        except Exception as err:
            end_time = default_timer()
            error_response = APIResponse(
                success=False,
                data=ErrorResponse(
                    error_code=1,
                    error_message=str(err)
                )
            )
            error = error_response.dict()
            return jsonify(error) 
    
    
    def buyitem(self, item_id, cantidad):
        try:
            start_time = default_timer()
            self.log.info("Funcion: %r - Paquete: %r - Mensaje: Inicio de transacción", "buyitem", __name__)  
            item_use_case = ItemUseCase()
            item_get_id = item_use_case.get_item(item_id)
            if item_get_id:
                item_get_id.stock -= cantidad
                item_updated = item_use_case.update(request=item_get_id, item_id=item_id)
                api_response = APIResponse(success=True, data=item_updated)
                response = api_response.dict()
                end_time = default_timer()
                self.log.info("Funcion: %r - Paquete: %r - Mensaje: Fin de transacción, procesada en: %r milisegundos", "buyitem", __name__, round(end_time - start_time)* 1000)
                return jsonify(response)
        except Exception as err:
            end_time = default_timer()
            error_response = APIResponse(
                success=False,
                data=ErrorResponse(
                    error_code=1,
                    error_message=str(err)
                )
            )
            error = error_response.dict()
            return jsonify(error)

        
        
        