"""API endpoints views.
The main logic for each of the API endpoints which getsexecuted when someone calls the API endpoints

* Author: Mahmoud Ibrahim
* Date: 20/6/2022
"""


from django.core.exceptions import ObjectDoesNotExist
from rest_framework import authentication
from plans.models import Plan
from .serializers import PlanSerializer
from rest_framework import authentication
from rest_framework import parsers
from rest_framework.serializers import ValidationError
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status


class PlanViewSet(viewsets.ViewSet):
    """Application View sets that describe the API endpoints logic.
       The Application API contains the following set of endpoints
       GET:  that get the list of the plans or a single plan if the PK is provided
       """

    # global variables initialization
    serializer_class = PlanSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Plan.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [parsers.JSONParser]

    #
    # override the get serializer method
    def get_serializer(self):
        return PlanSerializer()

    #
    #
    # list all apps of a user
    def list(self, request):
        """
        List all apps
        """
        if request.method != 'GET':
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

        plans = Plan.objects.all()
        serializer = PlanSerializer(plans, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    #
    #
    # method for get a single item
    def retrieve(self, request, pk):
        """
        get a single app by PK
        """
        if request.method != 'GET':
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

        try:
            app = Plan.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PlanSerializer(app)
        return Response(serializer.data, status=status.HTTP_200_OK)
