from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt
from api import views


urlpatterns = [
    path('get_menu', views.GetMenu.as_view({'get': 'list'})),
    path('get_item/<int:item_id>', views.get_item, name='get_item'),
    path('get_item_extras', views.GetItemExtras.as_view({'get': 'list'})),
    path('create_order', views.CreateOrder.as_view()),



]