from django.test import TestCase
from rest_framework.test import APIClient
import json
from django.core import serializers
from apps.api.v1.serializers import AppSerializer
from apps.models import App
import logging
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import render


@login_required(login_url='/users/login')
def secure(request):
    user = request.user
    return render(request, 'secure.html', {'email': user.email})

class AppTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.app = App()
        self.logger = logging.getLogger(__name__)
        User = get_user_model()
        User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')
        self.app = {
            "name": "Test App",
            "description": "Test Application",
            "type": "Web",
            "framework": "Django",
            "domain_name": "test.com"
        }
        authenticated = self.client.login(email="temporary@gmail.com", password="temporary")
        self.assertEqual(authenticated, True)

    def tearDown(self):
        self.client.logout()

    def test_create_request(self):
        """Test App creation for a app"""
        response = self.client.post('/api/v1/app/', self.app, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(App.objects.get().name, self.app["name"])

    def test_create_bad_request_type(self):
        """Test App creation for a app"""
        self.app['type'] = "test"
        response = self.client.post('/api/v1/app/', self.app, format='json')
        self.assertEqual(response.status_code, 400)

    def test_create_bad_request_framework(self):
        """Test App creation for a app"""
        self.app['framework'] = "test"
        response = self.client.post('/api/v1/app/', self.app, format='json')
        self.assertEqual(response.status_code, 400)

    def test_list(self):
        """Test App get for a app"""
        self.test_create_request()
        response = self.client.get('/api/v1/app/', format='json')
        self.assertEqual(self.app["name"], response.json()[0]["name"])

    def test_retrieve_exists(self):
        """Test App get for a app"""
        self.test_create_request()
        id = App.objects.get().id
        response = self.client.get('/api/v1/app/'+str(id)+'/', format='json')
        self.assertEqual(self.app["name"], response.json()["name"])

    def test_retrieve_not_exists(self):
        """Test App get for a app"""
        self.test_create_request()
        response = self.client.get('/api/v1/app/100/', format='json')
        self.assertEqual(response.status_code, 404)


    def test_update_request(self):
        """Test App update for a app"""
        self.test_create_request()
        id = App.objects.get().id
        self.app["name"] = "Updated Name"
        response = self.client.put('/api/v1/app/'+str(id)+'/', self.app, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["name"], self.app["name"])

    def test_update_bad_request(self):
        """Test App update for a app"""
        self.test_create_request()
        id = App.objects.get().id
        original_type = self.app['type']
        self.app['type'] = "test"
        response = self.client.put('/api/v1/app/'+str(id)+'/', self.app, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(App.objects.get().type, original_type)

    def test_update_invalid_app_id(self):
        """Test App update with Invalid app id"""
        self.test_create_request()
        self.app['type'] = "test"
        response = self.client.put('/api/v1/app/100/', self.app, format='json')
        self.assertEqual(response.status_code, 404)

    def test_partial_update_request(self):
        """Test App partial update for a app"""
        self.test_create_request()
        id = App.objects.get().id
        app = {
            "name": "Updated Name",
            "type": "Web",
            "framework": "Django",
        }
        response = self.client.patch('/api/v1/app/'+str(id)+'/', app, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["name"], app["name"])
        self.assertEqual(App.objects.get().domain_name, self.app["domain_name"])   # check old data to be retained

    def test_partial_update_bad_request(self):
        """Test App partial update for a app"""
        self.test_create_request()
        id = App.objects.get().id
        original_type = self.app['type']
        self.app['type'] = "test"
        response = self.client.patch('/api/v1/app/'+str(id)+'/', self.app, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(App.objects.get().type, original_type)

    def test_partial_update_invalid_app_id(self):
        """Test App partial update with Invalid app id"""
        self.test_create_request()
        self.app['type'] = "test"
        response = self.client.patch('/api/v1/app/100/', self.app, format='json')
        self.assertEqual(response.status_code, 404)

    def test_delete_request(self):
        """Test App delete for a app"""
        self.test_create_request()
        id = App.objects.get().id
        response = self.client.delete('/api/v1/app/'+str(id)+'/', format='json')
        self.assertEqual(response.status_code, 204)

    def test_delete_invalid_app_id(self):
        """Test App delete with Invalid app id"""
        self.test_create_request()
        self.app['type'] = "test"
        response = self.client.patch('/api/v1/app/100/', self.app, format='json')
        self.assertEqual(response.status_code, 404)



