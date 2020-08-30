class User():
    def __init__(self, 
    id, 
    name, 
    last_name, 
    email, 
    password, 
    phone_number, 
    address,
    profile_image,
    city_id,
    account_type_id,
    location,
    created_at,
    updated_at,
    active):
        self.id = id
        self.name = name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.phone_number = phone_number
        self.address = address
        self.profile_image = profile_image
        self.city_id = city_id
        self.account_type_id = account_type_id
        self.location = location
        self.created_at = created_at
        self.updated_at = updated_at
        self.active = active

class RoomType():
    def __init__(self, 
    room_type_id,
    room_type_desc):

        self.id = room_type_id
        self.room_type_desc = room_type_desc

