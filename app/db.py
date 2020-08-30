import pymysql.cursors
from app.booking.models import User

# Connect to the database
host='localhost'
db_user='root'
password='1234'
db='booking_project'
charset='utf8'
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
                             cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            e = 'none'
            # Create a new record
            sql = "INSERT INTO `users` (`name`, \
                                        `last_name`, \
                                        `email`, \
                                        `user_password`, \
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
                {user.phone_number},\
                "{user.address}",\
                "{user.profile_image}",\
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