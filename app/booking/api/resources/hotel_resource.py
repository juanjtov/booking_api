import json

from flask import jsonify, request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from app.db import get_hotels_by_name


class HotelResource(Resource):
    """
    """
    @jwt_required
    def get(self):
        body = request.get_json()
        hotel_name = body.get('name')
        hotels_fetched = get_hotels_by_name(hotel_name)
        return hotels_fetched, 200

    @jwt_required
    def post(self):
        pass

    @jwt_required
    def put(self):
        pass

    @jwt_required
    def delete(self):
        pass