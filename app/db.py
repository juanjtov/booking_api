import pymysql.cursors
from app.booking.models import User

# Connect to the database

host='35.196.253.142'
db_user='root'
password='x6iBKeMeDPyOuj9k'
db='booking_project'
charset='utf8'
db_connection_name = 'bookingapp-288110:us-east1:bookingdb'
cursorclass=pymysql.cursors.DictCursor


def set_user(user):
    """
    param: User object
    returns the MySQL error handle by the try-except senteces
    """

    
    connection = pymysql.connect(host=host,
                             user=db_user,
                             password=password,
                             db=db,
                             charset=charset,
                             unix_socket = '/cloudsql/{}'.format(db_connection_name),
                             cursorclass=pymysql.cursors.DictCursor)
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
    connection = pymysql.connect(host=host,
                             user=db_user,
                             password=password,
                             db=db,
                             charset=charset,
                             unix_socket = '/cloudsql/{}'.format(db_connection_name),
                             cursorclass=pymysql.cursors.DictCursor)
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
    connection = pymysql.connect(host=host,
                             user=db_user,
                             password=password,
                             db=db,
                             charset=charset,
                             unix_socket = '/cloudsql/{}'.format(db_connection_name),
                             cursorclass=pymysql.cursors.DictCursor)
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

def update_user(user):
    """
    param: User object
    returns the MySQL error handle by the try-except senteces
    """

    
    connection = pymysql.connect(host=host,
                             user=db_user,
                             password=password,
                             db=db,
                             charset=charset,
                             unix_socket = '/cloudsql/{}'.format(db_connection_name),
                             cursorclass=pymysql.cursors.DictCursor)
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

    
    connection = pymysql.connect(host=host,
                             user=db_user,
                             password=password,
                             db=db,
                             charset=charset,
                             unix_socket = '/cloudsql/{}'.format(db_connection_name),
                             cursorclass=pymysql.cursors.DictCursor)
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

def get_countries():
    """
    returns 
    """
    result = {}
    connection = pymysql.connect(host=host,
                             user=db_user,
                             password=password,
                             db=db,
                             charset=charset,
                             unix_socket = '/cloudsql/{}'.format(db_connection_name),
                             cursorclass=pymysql.cursors.DictCursor)
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
    connection = pymysql.connect(host=host,
                             user=db_user,
                             password=password,
                             db=db,
                             charset=charset,
                             unix_socket = '/cloudsql/{}'.format(db_connection_name),
                             cursorclass=pymysql.cursors.DictCursor)
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
    connection = pymysql.connect(host=host,
                             user=db_user,
                             password=password,
                             db=db,
                             charset=charset,
                             unix_socket = '/cloudsql/{}'.format(db_connection_name),
                             cursorclass=pymysql.cursors.DictCursor)
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