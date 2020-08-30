import json
from collections import namedtuple
from json import JSONEncoder

from flask import request, Blueprint, jsonify
from flask_restful import Api, Resource

from ..models import User
from app.common.error_handling import ObjectNotFound
from app.db import set_user

booking_app = Blueprint('booking_app', __name__)

api = Api(booking_app)

class UserResource(Resource):
    """ API UserResource

    Methods:
        get: HTTP Method
        post: HTTP Methods
    """    
    def get(self):
        user = User(1,
                    'Julian',
                    'Santos', 
                    'ingjuliansantos@gmail.com',
                    '123*',
                    '+573013787020',
                    'Carrera tal con calle x',
                    'img',
                    1125,
                    1,
                    0,0,
                    '','',True)

        s = jsonify(user.__dict__)

        return s

    def post(self):
        post_data = request.get_json()
        data_dict = json.loads(json.dumps(post_data))

        user = User(**data_dict)
        
        print('\nUser: ', user.name)
        
        e = set_user(user)

        return {'msg': 'User added'}

class RoomTypeResource(Resource):
    """ API RoomTypeResource

    Methods:
        get: HTTP Method
        post: HTTP Methods
    """  
    def get(self):
        pass

    def post(self):
        pass


api.add_resource(UserResource, '/api/booking/users', endpoint='users_resource')
api.add_resource(RoomTypeResource, '/api/booking/room_type', endpoint='room_type_resource')
