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


def get_hotels_by_name(name):
    """
    param: hotel name

    returns: 
    """
    result = {}
    connection = _connect_to_db()

    try:
        with connection.cursor() as cursor:
            e = 'none'
            sql = f"SELECT * FROM hotels WHERE `name` LIKE '%{name}%'"
            n = cursor.execute(sql)
            results = cursor.fetchall()
            for result in results:
                result['created_at'] = str(result['created_at'])
                result['updated_at'] = str(result['updated_at'])
    except Exception as ex:
        e = ex.args[0]
    finally:
        connection.close()
        return results, e
