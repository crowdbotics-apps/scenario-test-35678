"""API endpoints URLs.
The Urls of the API endpoints and their views handler which provide the API with the logic

* Author: Mahmoud Ibrahim
* Date: 20/6/2022
"""


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import PlanViewSet


#
# creating the API default rounter with an '/plan/' to the path
#
router = DefaultRouter()
router.register("plan", PlanViewSet)

#
# Registering the url to the expected paths
#
urlpatterns = [
    path("", include(router.urls)),
]
