from django.test import TestCase
from rest_framework.test import APIClient
from apps.models import App
import logging
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import render
from subscriptions.models import Subscription


@login_required(login_url='/users/login')
def secure(request):
    user = request.user
    return render(request, 'secure.html', {'email': user.email})


class SubscriptionTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.app = Subscription()
        self.logger = logging.getLogger(__name__)
        User = get_user_model()
        user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')
        App(user=user, name="App", type="Web", framework="Django").save()
        self.subscription = {
                              "plan": 1,
                              "app": App.objects.get().id,
                              "active": True
                            }
        authenticated = self.client.login(email="temporary@gmail.com", password="temporary")
        self.assertEqual(authenticated, True)

    def tearDown(self):
        self.client.logout()

    def test_create_request(self):
        """Test App creation for a subscription"""
        response = self.client.post('/api/v1/subscription/', self.subscription, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Subscription.objects.get().app.id, self.subscription["app"])

    def test_create_bad_request_plan(self):
        """Test App creation for a app"""
        self.subscription['plan'] = 1000
        response = self.client.post('/api/v1/subscription/', self.subscription, format='json')
        self.assertEqual(response.status_code, 400)

    def test_create_bad_request_app(self):
        """Test App creation for a app"""
        self.subscription["app"] = 1000
        response = self.client.post('/api/v1/subscription/', self.subscription, format='json')
        self.assertEqual(response.status_code, 400)

    def test_list(self):
        """Test App get for a app"""
        self.test_create_request()
        response = self.client.get('/api/v1/subscription/', format='json')
        self.assertEqual(self.subscription["plan"], response.json()[0]["plan"])

    def test_retrieve_exists(self):
        """Test App get for a app"""
        self.test_create_request()
        id = Subscription.objects.get().id
        response = self.client.get('/api/v1/subscription/'+str(id)+'/', format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.subscription["plan"], response.json()["plan"])

    def test_retrieve_not_exists(self):
        """Test App get for a app"""
        self.test_create_request()
        response = self.client.get('/api/v1/subscription/100/', format='json')
        self.assertEqual(response.status_code, 404)

    def test_update_request(self):
        """Test App update for a app"""
        self.test_create_request()
        id = Subscription.objects.get().id
        self.subscription["plan"] = 2
        response = self.client.put('/api/v1/subscription/'+str(id)+'/', self.subscription, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["plan"], self.subscription["plan"])

    def test_update_bad_request(self):
        """Test App update for a app"""
        self.test_create_request()
        id = Subscription.objects.get().id
        original_type = self.subscription['plan']
        self.subscription['plan'] = 1000
        response = self.client.put('/api/v1/subscription/'+str(id)+'/', self.subscription, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Subscription.objects.get().plan.id, original_type)

    def test_update_invalid_subscription_id(self):
        """Test App update with Invalid app id"""
        self.test_create_request()
        self.subscription["plan"] = 2
        response = self.client.put('/api/v1/subscription/1000/', self.subscription, format='json')
        self.assertEqual(response.status_code, 404)

    def test_partial_update_request(self):
        """Test App partial update for a app"""
        self.test_create_request()
        id = Subscription.objects.get().id
        subscription = {
                            "plan": 3,
                            "app": App.objects.get().id,
                            "active": True
                        }
        response = self.client.patch('/api/v1/subscription/'+str(id)+'/', subscription, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["plan"], subscription["plan"])
        self.assertEqual(Subscription.objects.get().app.id, self.subscription["app"])  # check old data to be retained

    def test_partial_update_bad_request(self):
        """Test App partial update for a app"""
        self.test_create_request()
        id = Subscription.objects.get().id
        original_plan = self.subscription['plan']
        self.subscription['plan'] = 100
        response = self.client.patch('/api/v1/subscription/'+str(id)+'/', self.subscription, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Subscription.objects.get().plan.id, original_plan)

    def test_partial_update_invalid_subs_id(self):
        """Test App partial update with Invalid app id"""
        self.test_create_request()
        self.subscription['plan'] = 2
        response = self.client.patch('/api/v1/subscription/100/', self.subscription, format='json')
        self.assertEqual(response.status_code, 404)
