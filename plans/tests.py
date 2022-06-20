from django.test import TestCase
from rest_framework.test import APIClient
from apps.models import App
import logging
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import render

from plans.models import Plan


@login_required(login_url='/users/login')
def secure(request):
    user = request.user
    return render(request, 'secure.html', {'email': user.email})


class PlanTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.plan = Plan()
        self.logger = logging.getLogger(__name__)
        User = get_user_model()
        User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')
        authenticated = self.client.login(email="temporary@gmail.com", password="temporary")
        self.assertEqual(authenticated, True)
        self.plan = {
                      "id": 1,
                      "name": "Free",
                      "description": "Test Free plan",
                      "price": "0",
                      "created_at": "2022-06-18T11:26:07.807692Z",
                      "updated_at": "2022-06-18T11:26:07.807692Z"
                    }

    def tearDown(self):
        self.client.logout()

    def test_list(self):
        """Test App get for a app"""
        response = self.client.get('/api/v1/plan/', format='json')
        self.assertEqual(self.plan["name"], response.json()[0]["name"])

    def test_retrieve_exists(self):
        """Test App get for a app"""
        response = self.client.get('/api/v1/plan/1/', format='json')
        self.assertEqual(self.plan["name"], response.json()["name"])

    def test_retrieve_not_exists(self):
        """Test App get for a app"""
        response = self.client.get('/api/v1/plan/100/', format='json')
        self.assertEqual(response.status_code, 404)



