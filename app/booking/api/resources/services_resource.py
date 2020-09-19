import json

from flask import jsonify, request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from app.db import get_services_by_hotel, set_service, update_service, delete_service
from app.booking.models import Service


class ServicesResource(Resource):
    """
    """
    @jwt_required
    def get(self):
        body = request.get_json()
        hotel_id = int(body.get('hotel_id'))
        services_fetched, e = get_services_by_hotel(hotel_id)

        services = []
        for service in services_fetched:
            print(service)
            services.append(Service(**service))

        return jsonify(services=[service.serialize() for service in services])

    @jwt_required
    def post(self):
        body = request.get_json()
        service = Service(**body)

        process_msg, e = set_service(service)
        if e != 1062:
            return process_msg
        else:
            return {'error': f'Service {service.name} already exists'}


    @jwt_required
    def put(self):
        body = request.get_json()
        service = Service(**body)

        process_msg, e = update_service(service)
        return process_msg

    @jwt_required
    def delete(self):
        body = request.get_json()
        service_id = int(body.get('service_id'))
        process_msg = delete_service(service_id)
        return process_msg