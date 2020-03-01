# SIMPLE CRUD API FOR CREATING TICKETS

This ticket system is design to log a ticket for a problem with a vod asset.  I was created using Python and Django framework

There are 3 basic fields

Field |Desc
-- | -- 
`problem_desc`  |  This problem you are having 
`asset_name`    |  The name of the vod title
`asset_id`      |  The asset ID 
`creator`       |  The userid associated with the ticket creation

You can perform the basic CRUD operations on the ticket

Operation |Desc
-- | -- 
`Create` | Create a new incident/ticket
`Read`   | Get a single ticket or list of all tickets
`Update` | Change paramaters of an exisitng ticket
`Delete` | Delete a ticket


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
	pip install coverage
```


Start the Django server with 

```
python3.7 manage.py runserver 0.0.0.0:8000
```

## TESTING 
test cases are located in /tkt_system/test.py

Run

```
coverage run manage.py test
```

Report
```
coverage report -m
```

## REST ENDPOINT DESCRIPTION AND CURL COMMANDS




CREATE ACCOUNT TO GET TOKEN  http://localhost:8000/rest-auth/registration/ 

```
curl -d "username=adam&password1=bogus12345&password2=bogus12345" -X POST http://localhost:8000/rest-auth/registration/ 
```


GET TOKEN  http://localhost:8000/rest-auth/login/


```
curl -d "username=adam&password=bogus12345" -X POST http://localhost:8000/rest-auth/login/
```


CREATE A TICKET http://localhost:8000/api/v1/tickets/


```
curl  -X POST -d "problem_desc='asset won't play'&asset_name='matrix reloaded'&asset_id=XYX123" http://localhost:8000/api/v1/tickets/ -H 'Authorization: Token 8bdac90872d706180f0082b371fe2ee760515bc1'
```

READ/GET ALL TICKETS http://localhost:8000/api/v1/tickets/
```
curl  -X GET http://localhost:8000/api/v1/tickets/ -H 'Authorization: Token 8bdac90872d706180f0082b371fe2ee760515bc1'
```




READ/GET A SINGLE TICKET http://localhost:8000/api/v1/tickets/:ID
```
curl  -X GET http://localhost:8000/api/v1/tickets/1 -H 'Authorization: Token 8bdac90872d706180f0082b371fe2ee760515bc1'
```

DELETE
```
curl  -X DELETE http://localhost:8000/api/v1/tickets/1 -H 'Authorization: Token 8bdac90872d706180f0082b371fe2ee760515bc1'
```

PUT/MODIFY A TICKET http://localhost:8000/api/v1/tickets/:ID

```
curl  -X PUT -d "problem_desc='asset freezes'&asset_name='matrix reloaded'&asset_id=XYX123" http://localhost:8000/api/v1/tickets/1 -H 'Authorization: Token 8bdac90872d706180f0082b371fe2ee760515bc1'
```

PAGINATION http://localhost:8000/api/v1/tickets/?page=<page no>

Page Sizes are set to 10 items.   You can access the next page with page=x
```
curl  -X GET http://localhost:8000/api/v1/tickets/?page=1 -H 'Authorization: Token 8bdac90872d706180f0082b371fe2ee760515bc1'
```


