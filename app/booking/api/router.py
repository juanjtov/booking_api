
from flask import Blueprint
from flask_restful import Api
from flask_cors import CORS
from .resources.user_resource import UserResource
from .resources.auth_resource import SignupApi, LoginApi
from .resources.room_type_resource import RoomTypeResource
from .resources.places_resource import PlacesResource

booking_app = Blueprint('booking_app', __name__)

api = Api(booking_app)
cors = CORS(booking_app, resources={r"/api/*": {"origins": "*"}})

api.add_resource(UserResource, '/api/booking/users', endpoint='users_resource')
api.add_resource(RoomTypeResource, '/api/booking/room_type', endpoint='room_type_resource')
api.add_resource(SignupApi, '/api/auth/signup')
api.add_resource(LoginApi, '/api/auth/login')
api.add_resource(PlacesResource, '/api/booking/places', '/api/booking/places/<string:place_type>')
