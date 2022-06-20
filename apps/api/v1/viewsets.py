"""API endpoints views.
The main logic for each of the API endpoints which getsexecuted when someone calls the API endpoints

* Author: Mahmoud Ibrahim
* Date: 20/6/2022
"""


from django.core.exceptions import ObjectDoesNotExist
from rest_framework import authentication
from rest_framework import parsers
from rest_framework.serializers import ValidationError
from apps.api.v1.serializers import AppSerializer
from apps.models import App
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
import logging

from subscriptions.models import Subscription


class AppViewSet(viewsets.ViewSet):
    """Application View sets that describe the API endpoints logic.
    The Application API contains the following set of endpoints
    POST: that created a new application
    GET:  that get the list of the application or a single application if the PK is provided
    PUT: update an application
    PATCH: Partial update for the application
    DELETE: delete a single application
    """

    # global variables initialization
    serializer_class = AppSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [parsers.JSONParser]
    logger = logging.getLogger(__name__)

    #
    # override the get serializer method
    def get_serializer(self):
        return AppSerializer()

    #
    #
    # list all apps of a user
    def list(self, request):
        """
        List all apps
        """
        if request.method != 'GET':
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

        apps = App.objects.filter(user=request.user)
        serializer = AppSerializer(apps, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    #
    #
    # method for get a single item
    def retrieve(self, request, pk):
        """
        Get a single app by PK
        """
        if request.method != 'GET':
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

        try:
            app = App.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            subscription = Subscription.objects.get(app=pk)
            app.subscription = subscription
        except ObjectDoesNotExist:
            pass

        serializer = AppSerializer(app)
        return Response(serializer.data, status=status.HTTP_200_OK)

    #
    #
    # add app
    def create(self, request, *args, **kwargs):
        """
        Create an application
        """
        if request.method != 'POST':
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

        try:
            serializer = AppSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=self.request.user)
        except ValidationError:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    #
    #
    # update app
    def update(self, request, pk):
        """
        Update a single app by PK
        """
        if request.method != 'PUT':
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

        try:
            serializer = AppSerializer(data=request.data)
            app = App.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            serializer.is_valid(raise_exception=True)
            serializer.update(app, serializer.validated_data)
        except ValidationError:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_200_OK)

    #
    #
    # partial update app
    def partial_update(self, request, pk):
        """
        Partial update a single app by PK
        """
        if request.method != 'PATCH':
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

        try:
            serializer = AppSerializer(data=request.data)
            app = App.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            serializer.is_valid(raise_exception=True)
            serializer.update(app, serializer.validated_data)
        except ValidationError:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_200_OK)

    #
    #
    # delete and remove app
    def destroy(self, request, pk):
        """
        Delete a single app by PK
        """
        if request.method != 'DELETE':
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

        try:
            app = App.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        app.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
