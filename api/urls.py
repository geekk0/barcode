from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt
from api import views


urlpatterns = [
    path('get_menu', views.GetMenu.as_view({'get': 'list'})),



]