from flask import jsonify, request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from app.booking.models import BedType
from app.db import get_bed_type, set_bed_type, update_bed_type, delete_bed_type, update_fields_bed_type


class BedTypeResource(Resource):
    """
    """
    @jwt_required
    def get(self):
        body = request.get_json()
        bed_type_id = body['bed_type_id']
        result = get_bed_type(bed_type_id)
        return result

    @jwt_required
    def post(self):
        body = request.get_json()
        bed_type = BedType(**body)
        result = set_bed_type(bed_type)
        return result

    @jwt_required
    def put(self):
        body = request.get_json()
        bed_type = BedType(**body)
        result = update_bed_type(bed_type)
        return result

    @jwt_required
    def delete(self):
        body = request.get_json()
        bed_type_id = body['bed_type_id']
        result = delete_bed_type(bed_type_id)
        return result

    @jwt_required
    def patch(self):
        body = request.get_json()
        bed_type = BedType(**body)
        print(bed_type.__dict__)
        result = update_fields_bed_type(bed_type)
        return result