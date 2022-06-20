"""API endpoints views.
The main logic for each of the API endpoints which getsexecuted when someone calls the API endpoints

* Author: Mahmoud Ibrahim
* Date: 20/6/2022
"""


from django.core.exceptions import ObjectDoesNotExist

from apps.models import App
from subscriptions.models import Subscription
from .serializers import SubscriptionSerializer
from rest_framework import authentication
from rest_framework import parsers
from rest_framework.serializers import ValidationError
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
import logging


class SubscriptionViewSet(viewsets.ViewSet):
    """subscription View sets that describe the API endpoints logic.
       The subscription API contains the following set of endpoints
       POST: that created a new subscription
       GET:  that get the list of the subscription or a single subscription if the PK is provided
       PUT: update an subscription
       PATCH: Partial update for the subscription
       """

    serializer_class = SubscriptionSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Subscription.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [parsers.JSONParser]
    logger = logging.getLogger(__name__)

    #
    # override the get serializer
    def get_serializer(self):
        return SubscriptionSerializer()

    #
    #
    # list all subscription of a user
    def list(self, request):
        """
        List all subscription
        """
        if request.method != 'GET':
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

        apps = Subscription.objects.filter(user=request.user)
        serializer = SubscriptionSerializer(apps, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    #
    #
    # method for get a single item
    def retrieve(self, request, pk):
        """
        get a single subscription by PK
        """
        if request.method != 'GET':
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

        try:
            subscription = Subscription.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = SubscriptionSerializer(subscription)
        return Response(serializer.data, status=status.HTTP_200_OK)

    #
    #
    # add subscription
    def create(self, request):
        """
        create an subscription
        """

        if request.method != 'POST':
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

        try:
            serializer = SubscriptionSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=request.user)
        except ValidationError:
            self.logger.warning(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    #
    #
    # update subscription
    def update(self, request, pk):
        """
        update a single subscription by PK
        """
        if request.method != 'PUT':
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

        try:
            serializer = SubscriptionSerializer(data=request.data)
            subscription = Subscription.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            serializer.is_valid(raise_exception=True)
            serializer.update(subscription, serializer.validated_data)
        except ValidationError:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_200_OK)

    #
    #
    # partial update subscription
    def partial_update(self, request, pk):
        """
        patch a single subscription by PK
        """
        if request.method != 'PATCH':
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

        serializer = SubscriptionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            subscription = Subscription.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            serializer.is_valid(raise_exception=True)
            serializer.update(subscription, serializer.validated_data)
        except ValidationError:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_200_OK)

