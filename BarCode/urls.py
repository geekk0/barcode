from django.contrib import admin
from django.urls import path, include
from bar import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', include('bar.urls')),
    path('login/', views.LoginView.as_view()),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)