from flask import jsonify
import json
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from app.db import get_countries, get_states, get_cities
from app.booking.models import Country, State, City

class PlacesResource(Resource):

    @jwt_required
    def get(self, place_type):
        countries= []
        if place_type=='country':
            result, e = get_countries()
            
            countries = []
            for c in result:
                country = Country(**c)
                countries.append(country)

            return  jsonify(countries=[country.serialize() for country in countries])
        elif place_type=='state':
            result, e = get_states()
            
            states = []
            for s in result:
                state = State(**s)
                states.append(state)

            return  jsonify(states=[state.serialize() for state in states])
        elif place_type=='city':
            result, e = get_cities()
            
            cities = []
            for c in result:
                city = City(**c)
                cities.append(city)

            return  jsonify(cities=[city.serialize() for city in cities])
        else:
            return jsonify({'error': 'place type unknown'})
