from bar.models import ItemCard, Order, Extras
from rest_framework import viewsets
from rest_framework import permissions
from api.serializer import MenuSerializer, ExtraSerializer
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from datetime import date, datetime
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view


class GetMenu(viewsets.ModelViewSet):

    def get_queryset(self):
        menu_queryset = ItemCard.objects.filter(available=True)

        return menu_queryset

    def get_serializer_class(self):
        serializer_class = MenuSerializer
        return serializer_class

    """def get_permissions(self):
        permission_classes = [permissions.IsAuthenticated()]
        return permission_classes"""


@api_view(['GET'])
def get_item(request, item_id):
    item_object = ItemCard.objects.get(id=item_id)
    serializer = MenuSerializer(item_object)

    return Response(serializer.data, status=status.HTTP_200_OK)


class GetItemExtras(viewsets.ModelViewSet):

    def get_queryset(self):
        item_id = self.request.query_params.get('item_id')

        item_object = ItemCard.objects.get(id=item_id)

        extras = Extras.objects.filter(itemcard=item_object).order_by("list_number")

        return extras

    def get_serializer_class(self):
        serializer_class = ExtraSerializer
        return serializer_class











