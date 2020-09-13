from flask import jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required

class RoomTypeResource(Resource):
    """ API RoomTypeResource

    Methods:
        get: HTTP Method
        post: HTTP Methods
    """
    @jwt_required  
    def get(self):
        pass

    @jwt_required
    def post(self):
        pass
