import json

from flask import jsonify, request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from app.db import get_hotels_by_name, set_hotel, update_hotel, delete_hotel
from app.booking.models import Hotel


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
        body = request.get_json()
        hotel = Hotel(**body)
        process_msg = set_hotel(hotel)
        return process_msg

    @jwt_required
    def put(self):
        body = request.get_json()
        hotel = Hotel(**body)
        process_msg = update_hotel(hotel)
        return process_msg

    @jwt_required
    def delete(self):
        body = request.get_json()
        hotel_id = body['hotel_id']
        process_msg = delete_hotel(hotel_id)
        return process_msg

    @jwt_required
    def patch(self):
        pass