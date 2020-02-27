# SIMPLE CRUD API FOR CREATING TICKETS

## Requirements
- Python 3.6
- Django (2.1)
- Django REST Framework
- Django Rest Auth

## Installation
```
	pip install django
	pip install djangorestframework
	pip install django-rest-auth
	pip install django-allauth
        pip install django-extensions
```

## Structure

Contains a single resource tickets with the following methods 

Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`tickets` | GET | READ | Get all ticket
`tickets/:id` | GET | READ | Get a single ticket
`tickets`| POST | CREATE | Create a new ticket
`tickets/:id` | PUT | UPDATE | Update a ticket
`tickets/:id` | DELETE | DELETE | Delete a ticket

## HOW TO USE


Start the Django server with 

```
python3.7 manage.py runserver 0.0.0.0:8000
```


CREATE ACCOUNT TO GET TOKEN

```
curl -d "username=adam&password1=bogus12345&password2=bogus12345" -X POST http://localhost:8000/rest-auth/registration/ 
```


GET TOKEN 

```
curl -d "username=adam&password=bogus12345" -X POST http://localhost:8000/rest-auth/login/
```


CREATE A TICKET

```
curl  -X POST -d "problem_desc='asset won't play'&asset_name='matrix reloaded'&asset_id=XYX123" http://localhost:8000/api/v1/tickets/ -H 'Authorization: Token 8bdac90872d706180f0082b371fe2ee760515bc1'
```

READ/GET
```
curl  -X GET http://localhost:8000/api/v1/tickets/1 -H 'Authorization: Token 8bdac90872d706180f0082b371fe2ee760515bc1'
```

DELETE
```
curl  -X DELETE http://localhost:8000/api/v1/tickets/1 -H 'Authorization: Token 8bdac90872d706180f0082b371fe2ee760515bc1'
```

PUT/MODIFY

```
curl  -X PUT -d "problem_desc='asset freezes'&asset_name='matrix reloaded'&asset_id=XYX123" http://localhost:8000/api/v1/tickets/1 -H 'Authorization: Token 8bdac90872d706180f0082b371fe2ee760515bc1'
```



PAGINATION

Page Sizes are set to 10 items.   You can access the next page with page=x
```
curl  -X GET http://localhost:8000/api/v1/tickets/?page=1 -H 'Authorization: Token 8bdac90872d706180f0082b371fe2ee760515bc1'
```


