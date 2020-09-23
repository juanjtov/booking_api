from flask import jsonify, request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from app.booking.models import RoomType
from app.db import get_room_types, set_room_type, update_room_type, delete_room_type, update_fields_room_type

class RoomTypeResource(Resource):
    """ API RoomTypeResource

    Methods:
        get: HTTP Method
        post: HTTP Methods
    """
    @jwt_required  
    def get(self):
        body = request.get_json()
        room_type_id = body['room_type_id']
        room_type = get_room_types(room_type_id)
        return room_type

    @jwt_required
    def post(self):
        body = request.get_json()
        room_type = RoomType(**body)
        result = set_room_type(room_type)
        return result
    
    @jwt_required
    def put(self):
        body = request.get_json()
        room_type = RoomType(**body)
        result = update_room_type(room_type)
        return result

    @jwt_required
    def delete(self):
        body = request.get_json()
        room_type_id = body['room_type_id']
        result = delete_room_type(room_type_id)
        return result

    @jwt_required
    def patch(self):
        body = request.get_json()
        room_type = RoomType(**body)
        result = update_fields_room_type(room_type)
        return result