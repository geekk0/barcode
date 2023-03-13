from bar.models import ItemCard, Order, Extras
from rest_framework import viewsets
from rest_framework import permissions
from api.serializer import MenuSerializer, ExtraSerializer, OrderSerializer
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
from .bot import send_telegram_order_notification


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


class CreateOrder(APIView):

    def post(self, request):

        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            order_info = str(datetime.now().time())[:8] + " Поступил заказ, стол: '" + str(serializer.data['location']) + "'.\n" + "Состав заказа: \n" + ItemCard.objects.get(id=serializer.data['item']).name + "\nКоличество: " + \
                         str(serializer.data['quantity']) + "\nСахар: " + str(serializer.data['sugar']) + "\n" + "Дополнительно: " + \
                         get_extras_text(serializer.data['extras'])

            print(order_info)
            send_telegram_order_notification(order_info)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




def get_extras_text(list):

    extras_text = ""

    for extra_id in list:
        extra_name = Extras.objects.get(id=extra_id).name
        extras_text += extra_name + " "

    if len(extras_text) < 1:
        extras_text = "-"

    return extras_text


