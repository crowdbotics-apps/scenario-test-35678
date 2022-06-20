"""API endpoints URLs.
The Urls of the API endpoints and their views handler which provide the API with the logic

* Author: Mahmoud Ibrahim
* Date: 20/6/2022
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import SubscriptionViewSet


#
# creating the API default rounter with an '/app/' to the path
#
router = DefaultRouter()
router.register("subscription", SubscriptionViewSet)

#
# Registering the url to the expected paths
#
urlpatterns = [
    path("", include(router.urls)),
]
