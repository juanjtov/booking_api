import pymysql.cursors
from app.booking.models import User

# Connect to the database

HOST='remotemysql.com'
DB_USER='99eiAjcjXR'
PASSWORD='qxoChOlVS2'
DB='99eiAjcjXR'
CHARSET='utf8'
CURSORCLASS=pymysql.cursors.DictCursor


def _connect_to_db(
        host=HOST, port=3306,
        db_user=DB_USER, password=PASSWORD,
        db=DB, charset=CHARSET,
        cursorclass=CURSORCLASS):
    """Establish a connection to the DataBase
    """
    try:
        con = pymysql.connect(host=host, user=db_user, password=password, db=db, charset=charset, cursorclass=cursorclass)
        return con
    except Exception as e:
        print('Error: ', e)


def set_user(user):
    """
    param: User object
    returns the MySQL error handle by the try-except senteces
    """

    connection = _connect_to_db()

    try:
        with connection.cursor() as cursor:
            e = 'none'
            # Create a new record
            sql = "INSERT INTO `users` (`name`, \
                                        `last_name`, \
                                        `email`, \
                                        `password`, \
                                        `phone_number`, \
                                        `address`, \
                                        `profile_image_url`, \
                                        `city_id`, \
                                        `account_type_id`, \
                                        `lat_location`, \
                                        `long_location`, \
                                        `active`) "
            values = f"""VALUES ("{user.name}",\
                "{user.last_name}",\
                "{user.email}",\
                "{user.password}",\
                "{user.phone_number}",\
                "{user.address}",\
                "{user.profile_image_url}",\
                {user.city_id},\
                {user.account_type_id},\
                {user.lat_location},\
                {user.long_location},\
                {user.active})"""
            sql = sql + values
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()

    except Exception as ex:        
        print(ex.args[0])
        print(ex.args[1])
        e = ex.args[0]
    finally:
        connection.close()
        return e

def get_user(email):
    """
    param: username
    returns User instance with user data, the MySQL error handle by the try-except senteces
    """
    result = {}
    connection = _connect_to_db()

    try:
        with connection.cursor() as cursor:
            row_count = 0
            e = 'none'
            # Read a single record
            sql = f"SELECT `id`,`name`, \
                            `last_name`, \
                            `email`, \
                            `password`, \
                            `phone_number`, \
                            `address`, \
                            `profile_image_url`, \
                            `city_id`, \
                            `account_type_id`, \
                            `lat_location`, \
                            `long_location`, \
                            `created_at`, \
                            `updated_at`, \
                            `active` FROM users WHERE users.email='{email}'"
            cursor.execute(sql)
            result = cursor.fetchone()

    except Exception as ex:        
        #print(ex.args[1]) 
        e = ex.args[0]
    finally:
        connection.close()
        return  result,e

def get_user_for_login(email):
    """
    param: username
    returns User instance with user data, the MySQL error handle by the try-except senteces
    """
    result = {}
    connection = _connect_to_db()

    try:
        with connection.cursor() as cursor:
            row_count = 0
            e = 'none'
            # Read a single record
            sql = f"SELECT email, password, COUNT(email) AS row_count FROM users WHERE users.email='{email}'"
            cursor.execute(sql)
            result = cursor.fetchone()
    except Exception as ex:        
        #print(ex.args[1]) 
        e = ex.args[0]
    finally:
        connection.close()
        return  result,e


# Hotels functions section ----------------------------------------------------


def get_hotels_by_name(name):
    """
    param: hotel_name

    returns: a list of the hotels that matched the given name
    """
    result = {}
    connection = _connect_to_db()

    try:
        with connection.cursor() as cursor:
            e = 'none'
            sql = f"SELECT * FROM hotels \
                    WHERE `name` LIKE '%{name}%' AND `active`=1"
            cursor.execute(sql)
            results = cursor.fetchall()
            if results:
                for result in results:
                    result['check_out_hour'] = str(result['check_out_hour'])
                    result['created_at'] = str(result['created_at'])
                    result['updated_at'] = str(result['updated_at'])
    except Exception as ex:
        e = ex.args[0]
    finally:
        connection.close()
        return results


def set_hotel(hotel):
    """
    param: Hotel class

    returns: the hotel inserted into the database
    """

    connection = _connect_to_db()

    try:
        with connection.cursor() as cursor:
            e = 'none'
            insert_stmt = f'INSERT INTO hotels(`name`,\
                                               `address`, `city_id`, `user_id`,\
                                               `description`, `check_out_hour`,\
                                               `rooms_number`, `html_iframe`,\
                                               `policy`) VALUES '
            values = f'("{hotel.name}",\
                        "{hotel.address}",\
                        {hotel.city_id},\
                        {hotel.user_id},\
                        "{hotel.description}",\
                        {hotel.check_out_hour},\
                        {hotel.rooms_number},\
                        "{hotel.html_iframe}",\
                        "{hotel.policy}")'
            values = values.replace('""', 'NULL')
            sql = insert_stmt + values
            rows = cursor.execute(sql)
            if rows == 1:
                e = 201
            else:
                raise Exception('There was a problem creating your hotel!')

        connection.commit()
        msg = f'{hotel.name} succesfully saved!'

    except Exception as ex:
        e = ex.args[0]
        print(ex)
        msg = ex.args[1]
    finally:
        connection.close()
        return {'msg': msg}, e


def update_hotel(hotel):
    """
    param: dict object containing the hotel_id and the data to be updated

    returns: status message
    """
    connection = _connect_to_db()
    msg = ''
    e = 0

    try:
        with connection.cursor() as cursor:
            update_stmt = 'UPDATE hotels SET '
            values = f'`name` = "{hotel.name}",\
                       `address` = "{hotel.address}",\
                       `city_id` = {hotel.city_id},\
                       `user_id` = {hotel.user_id},\
                       `description` = "{hotel.description}",\
                       `check_out_hour` = "{hotel.check_out_hour}",\
                       `html_iframe` = "{hotel.html_iframe}",\
                       `policy` = "{hotel.policy}" '
            id_spec = f'WHERE `hotel_id` = {hotel.hotel_id}'
            sql = update_stmt + values + id_spec
            rows = cursor.execute(sql)
            if rows == 1:
                e = 200
                msg = f'{hotel.name} succesfully updated!'
            else:
                e = 404
                msg = f'Hotel id {hotel.hotel_id} not found or invalid!'

        connection.commit()
    except Exception as ex:
        print(ex)
    finally:
        connection.close()
        return {'msg': msg}, e


def delete_hotel(hotel):
    """
    """
    connection = _connect_to_db()
    msg = ''
    e = 0

    try:
        with connection.cursor() as cursor:
            update_stmt = 'UPDATE hotels SET '
            values = f'`active` = 0 '
            id_spec = f'WHERE `hotel_id` = {hotel.hotel_id} AND NOT `active` = 0'
            sql = update_stmt + values + id_spec
            rows = cursor.execute(sql)
            if rows == 1:
                e = 204
            else:
                msg = f'Hotel id {hotel.hotel_id} not found or invalid!'
                e = 404

        connection.commit()
    except Exception as ex:
        print(ex)
    finally:
        connection.close()
        if e == 204:
            return msg, e
        else:
            return {'msg': msg}, e


def update_user(user):
    """
    param: User object
    returns the MySQL error handle by the try-except senteces
    """
    
    connection = _connect_to_db()
  
    try:
        with connection.cursor() as cursor:
            e = 'none'

            print(user.email)
            print(user.name)
            print(user.phone_number)
            # Create a new record
            sql = f"""UPDATE `users` SET \
                                        `name` = "{user.name}", \
                                        `last_name` = "{user.last_name}", \
                                        `email` = "{user.email}", \
                                        `phone_number` = "{user.phone_number}", \
                                        `address` = "{user.address}", \
                                        `profile_image_url` = "{user.profile_image_url}", \
                                        `city_id` = {user.city_id}, \
                                        `account_type_id` = {user.account_type_id}, \
                                        `lat_location` = {user.lat_location}, \
                                        `long_location` = {user.long_location}, \
                                        `active` = {user.active} WHERE users.email = '{user.email}'"""
            
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()

    except Exception as ex:        
        print(ex.args[0])
        print(ex.args[1])
        e = ex.args[0]
    finally:
        connection.close()
        return e   

def update_user_password(user):
    """
    param: User object
    returns the MySQL error handle by the try-except senteces
    """

    
    connection = _connect_to_db()
    
    try:
        with connection.cursor() as cursor:
            e = 'none'

            print(user.email)
            print(user.password)
            
            # Create a new record
            sql = f"""UPDATE `users` SET `password` = "{user.password}" WHERE users.email = '{user.email}'"""
            
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()

    except Exception as ex:        
        print(ex.args[0])
        print(ex.args[1])
        e = ex.args[0]
    finally:
        connection.close()
        return e

# Places functions section -----------------------------------------------------

def get_countries():
    """
    returns 
    """
    result = {}
    connection = _connect_to_db()
  
    try:
        with connection.cursor() as cursor:
            row_count = 0
            e = 'none'
            # Read a single record
            sql = f"SELECT * FROM countries"
            cursor.execute(sql)
            result = cursor.fetchall()

    except Exception as ex:        
        #print(ex.args[1]) 
        e = ex.args[0]
    finally:
        connection.close()
        return  result,e

def get_states():
    """
    returns 
    """
    result = {}
    connection = _connect_to_db()

    try:
        with connection.cursor() as cursor:
            row_count = 0
            e = 'none'
            # Read a single record
            sql = f"SELECT * FROM states"
            cursor.execute(sql)
            result = cursor.fetchall()

    except Exception as ex:        
        #print(ex.args[1]) 
        e = ex.args[0]
    finally:
        connection.close()
        return  result,e

def get_cities():
    """
    returns 
    """
    result = {}
    connection = _connect_to_db()
  
    try:
        with connection.cursor() as cursor:
            row_count = 0
            e = 'none'
            # Read a single record
            sql = f"SELECT * FROM cities"
            cursor.execute(sql)
            result = cursor.fetchall()

    except Exception as ex:        
        #print(ex.args[1]) 
        e = ex.args[0]
    finally:
        connection.close()
        return  result,e


# Services functions section

def get_services_by_hotel(hotel_id):
    """
    returns 
    """
    result = {}
    connection = _connect_to_db()
  
    try:
        with connection.cursor() as cursor:
            row_count = 0
            e = 'none'
            # Read a single record
            sql = f"""SELECT * FROM services WHERE services.hotel_id = {hotel_id}"""
            cursor.execute(sql)
            result = cursor.fetchall()

    except Exception as ex:        
        #print(ex.args[1]) 
        e = ex.args[0]
    finally:
        connection.close()
        return  result,e

def set_service(service):
    """
    param: Hotel class

    returns: the hotel inserted into the database
    """

    connection = _connect_to_db()
    msg = ""
    try:
        with connection.cursor() as cursor:
            e = 'none'
            insert_stmt = f"""INSERT INTO services (`name`,\
                                               `image_url`,\
                                               `active`,\
                                               `hotel_id`,\
                                               `description`) VALUES """
            values = f"""('{service.name}',\
                        '{service.image_url}',\
                        {service.active},\
                        {service.hotel_id},\
                        '{service.description}')"""
            sql = insert_stmt + values
            rows = cursor.execute(sql)
            if rows == 1:
                e = 201
            else:
                raise Exception('There was a problem creating your hotel!')

        connection.commit()
        msg = f'{service.name} service succesfully saved!'

    except Exception as ex:
        e = ex.args[0]
        print(ex)
        msg = ex.args[1]
    finally:
        connection.close()
        return {'msg': msg}, e

def update_service(service):
    """
    param: dict object containing the hotel_id and the data to be updated

    returns: status message
    """
    connection = _connect_to_db()
    msg = ''
    e = 0

    try:
        with connection.cursor() as cursor:
            update_stmt = 'UPDATE services SET '
            values = f'`image_url` = "{service.image_url}",\
                       `active` = {service.active},\
                       `description` = "{service.description}" '
            id_spec = f'WHERE `service_id` = {service.service_id}'
            sql = update_stmt + values + id_spec
            rows = cursor.execute(sql)
            if rows == 1:
                e = 200
                msg = f'{service.name} was service succesfully updated!'
            else:
                e = 404
                msg = f'service id {service.service_id} was not found or is invalid!'

        connection.commit()
    except Exception as ex:
        print(ex)
    finally:
        connection.close()
        return {'msg': msg}, e

def delete_service(service_id):
    """
    """
    connection = _connect_to_db()
    msg = ''
    e = 0

    try:
        with connection.cursor() as cursor:
            update_stmt = 'UPDATE services SET '
            values = f'`active` = 0 '
            id_spec = f'WHERE `service_id` = {service_id} AND NOT `active` = 0'
            sql = update_stmt + values + id_spec
            rows = cursor.execute(sql)
            if rows == 1:
                e = 200
                msg = f'Service id {service_id} was deactivated correctly!'
            else:
                msg = f'Service id {service_id} was not found or is invalid!'
                e = 404

        connection.commit()
    except Exception as ex:
        print(ex)
    finally:
        connection.close()
        if e == 200:
            return {'msg': msg}, e
        else:
            return {'msg': msg}, e


# Reviwes functions

def get_reviews_by_hotel(hotel_id):
    """
    returns 
    """
    result = {}
    connection = _connect_to_db()
  
    try:
        with connection.cursor() as cursor:
            row_count = 0
            e = 'none'
            # Read a single record
            sql = f"""SELECT * FROM reviews WHERE reviews.hotel_id = {hotel_id}"""
            cursor.execute(sql)
            result = cursor.fetchall()

    except Exception as ex:        
        #print(ex.args[1]) 
        e = ex.args[0]
    finally:
        connection.close()
        return  result,e

def get_reviews_by_user(user_id):
    """
    returns 
    """
    result = {}
    connection = _connect_to_db()
  
    try:
        with connection.cursor() as cursor:
            row_count = 0
            e = 'none'
            # Read a single record
            sql = f"""SELECT * FROM reviews WHERE reviews.user_id = {user_id}"""
            cursor.execute(sql)
            result = cursor.fetchall()

    except Exception as ex:        
        #print(ex.args[1]) 
        e = ex.args[0]
    finally:
        connection.close()
        return  result,e

def set_review(review):
    """
    param: Hotel class

    returns: the hotel inserted into the database
    """

    connection = _connect_to_db()
    msg = ""
    try:
        with connection.cursor() as cursor:
            e = 'none'
            insert_stmt = f"""INSERT INTO reviews (`content`,\
                                               `user_id`,\
                                               `hotel_id`,\
                                               `active`) VALUES """
            values = f"""('{review.content}',\
                        {review.user_id},\
                        {review.hotel_id},\
                        {review.active})"""
            sql = insert_stmt + values
            rows = cursor.execute(sql)
            if rows == 1:
                e = 201
            else:
                raise Exception('There was a problem creating your hotel!')

        connection.commit()
        msg = f'Review succesfully saved!'

    except Exception as ex:
        e = ex.args[0]
        print(ex)
        msg = ex.args[1]
    finally:
        connection.close()
        return {'msg': msg}, e

def update_review(review):
    """
    param: dict object containing the hotel_id and the data to be updated

    returns: status message
    """
    connection = _connect_to_db()
    msg = ''
    e = 0

    try:
        with connection.cursor() as cursor:
            update_stmt = 'UPDATE reviews SET '
            values = f'`content` = "{review.content}"'
            id_spec = f'WHERE `review_id` = {review.review_id}'
            sql = update_stmt + values + id_spec
            rows = cursor.execute(sql)
            if rows == 1:
                e = 200
                msg = f'{review.review_id} was service succesfully updated!'
            else:
                e = 404
                msg = f'review id {review.review_id} was not found or is invalid!'

        connection.commit()
    except Exception as ex:
        print(ex)
    finally:
        connection.close()
        return {'msg': msg}, e

def delete_review(review_id):
    """
    """
    connection = _connect_to_db()
    msg = ''
    e = 0

    try:
        with connection.cursor() as cursor:
            update_stmt = 'UPDATE reviews SET '
            values = f'`active` = 0 '
            id_spec = f'WHERE `review_id` = {review_id} AND NOT `active` = 0'
            sql = update_stmt + values + id_spec
            rows = cursor.execute(sql)
            if rows == 1:
                e = 200
                msg = f'review_id {review_id} was deactivated correctly!'
            else:
                msg = f'review_id {review_id} was not found or is invalid!'
                e = 404

        connection.commit()
    except Exception as ex:
        print(ex)
    finally:
        connection.close()
        if e == 200:
            return {'msg': msg}, e
        else:
            return {'msg': msg}, e