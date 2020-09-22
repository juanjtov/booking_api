from flask import jsonify, request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from app.booking.models import Room
from app.db import set_room, get_rooms


class RoomResource(Resource):
    """
    """
    def get(self):
        body = request.get_json()
        result = get_rooms(body)
        return result

    @jwt_required
    def post(self):
        body = request.get_json()
        room = Room(**body)
        result = set_room(room)
        return result

    @jwt_required
    def put(self):
        body = request.get_json()
        pass

    @jwt_required
    def delete(self):
        body = request.get_json()
        pass

    @jwt_required
    def patch(self):
        body = request.get_json()
        pass