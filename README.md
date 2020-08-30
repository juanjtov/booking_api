# booking_api

La estrategia es crear un recurso de la API por cada tabla, de esa manera nuestros amigos del front pueden acceder a este recurso via una peticion HTTP con los verbos `GET`, `PUT` o `POST`.

## Ambiente Virtual y Arranque

1. Crear y activar un ambiente virtual con nombre `venv` y ejecutar:

```$ pip install -r requirements.txt ```

2. En el archivo del ambiente virtual ```venv/bin/activate``` agregar las siguientes lineas de código al fina del archivo:

```
export FLASK_APP="entrypoint:app"
export FLASK_ENV="development"
export APP_SETTINGS_MODULE="config.default"
```
3. Arrancar el servidor ejecutando:

```$ flask run```

En este punto ya deben poder ejecutar la API.

4. Relizar una peticion ```GET``` a la URL: ```http://localhost:5000/api/booking/users```
 y deben obtener la siguiente respuesta:

 ``` json
{
    "account_type_id": 1,
    "active": true,
    "address": "Carrera tal con calle x",
    "city_id": 1125,
    "created_at": "",
    "email": "platzimaster@gmail.com",
    "id": 1,
    "last_name": "Master",
    "lat_location": 0,
    "long_location": 0,
    "name": "Platzi",
    "password": "123*",
    "phone_number": "+573013787020",
    "profile_image": "img",
    "updated_at": ""
}
 ```
Este es un ejemplo, la idea es que lo puedan arrancar.

## ¿Como implementar un recurso de la API?

* Se debe implementar una clase por cada tabla en el archivo `models.py`
* En el archivo `resources.py` se debe implementar la clase de cada recurso, tambien se debe agregar a la app:

``` api.add_resource(UserResource, '/api/booking/users', endpoint='users_resource') ```

Como pueden ver en el codigo, ahí se define la URL de la API la idea es que quede ```/api/booking/<nombre_tabla>```

## ¿Qué hace falta?

1. Agregar envio de variables por la URL con el metodo ```GET```
2. Agregar BluePrint de autenticacion
3. Habilitar CORS, ya que nuestra API se va alojar en una instacia de App Engine diferente a donde va a estar la del Front End
4. Determinar si usamos tokens o con la implementacion de autenticacion de Flask es suficiente.
5. Cada recurso debe tener los siguientes metodos:
    * ```GET```: Para traer datos al front
    * ```POST```: Para enviar datos desde el front
    * ```PUT```: Para actualizar datos desde el front




