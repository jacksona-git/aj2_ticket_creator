from django.test import TestCase
from tkt_system.models import Ticket
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
import json


class TestPoll(APITestCase):
    valid_token = ""

    def setUp(self):
        self.username = 'admin'
        self.password = 'root1234'
        self.user = User.objects.create_user(username=self.username, password=self.password)



    def test_basic_login(self):
        print("Running tests for basic login ")

        self.client.login(username=self.username, password=self.password)
        response = self.client.post('/rest-auth/login/', {'username': 'admin', 'password' : 'root1234'},format='json')
        auth_info = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        
        
    def test_read_get(self):
        print("Running test for GET/READ request")
        self.client.login(username=self.username, password=self.password)
        response = self.client.post('/rest-auth/login/', {'username': 'admin', 'password' : 'root1234'},format='json')

        auth_info = json.loads(response.content)

        self.client.credentials(HTTP_AUTHORIZATION='Token ' +  auth_info['key'])
        response2 = self.client.get('/api/v1/tickets/', format='json')


        self.assertEqual(response2.status_code, 200)

