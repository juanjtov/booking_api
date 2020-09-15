from flask_bcrypt import generate_password_hash, check_password_hash


class UserLogin():
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')
    
    def check_password(self, password):
        return check_password_hash(self.password, password)

class User(UserLogin):
    def __init__(self, 
    id, 
    name, 
    last_name, 
    email, 
    password, 
    phone_number, 
    address,
    profile_image_url,
    city_id,
    account_type_id,
    lat_location,
    long_location,
    created_at,
    updated_at,
    active):
        self.id = id
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.profile_image_url = profile_image_url
        self.city_id = city_id
        self.account_type_id = account_type_id
        self.lat_location = lat_location
        self.long_location = long_location
        self.created_at = created_at
        self.updated_at = updated_at
        self.active = active
        super().__init__(email, password)

class RoomType():
    def __init__(self, 
    room_type_id,
    room_type_desc):

        self.id = room_type_id
        self.room_type_desc = room_type_desc


class Hotel():
    def __init__(self,
                 name,
                 address,
                 city_id,
                 user_id,
                 description,
                 check_out_hour,
                 rooms_number,
                 hotel_id=None,
                 html_iframe=None,
                 policy=None,
                 created_at=None,
                 updated_at=None,
                 active=None):
        self.name = name
        self.address = address
        self.description = description
        self.city_id = city_id
        self.user_id = user_id
        self.check_out_hour = check_out_hour
        self.rooms_number = rooms_number
        self.hotel_id = hotel_id
        self.html_iframe = html_iframe
        self.policy = policy
        self.created_at = created_at
        self.updated_at = updated_at
        self.active = active

class Country():
    def __init__(self,
    country_id, iso, name, spanish_name):
        self.country_id = country_id
        self.iso = iso
        self.name = name
        self.spanish_name = spanish_name

    def serialize(self):
        return {
            'country_id': self.country_id, 
            'iso': self.iso,
            'name': self.name,
            'spanish_name': self.spanish_name
        }

class State():
    def __init__(self, state_id, name, country_id):
        self.state_id = state_id
        self.name = name
        self.country_id = country_id

    def serialize(self):
        return {
            'state_id': self.state_id, 
            'name': self.name,
            'country_id': self.country_id
        }

class City():
    def __init__(self, city_id, name, state_id):
        self.city_id = city_id
        self.name = name
        self.state_id = state_id

    def serialize(self):
        return {
            'city_id': self.city_id, 
            'name': self.name,
            'state_id': self.state_id
        }
