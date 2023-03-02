from django.contrib import admin
from django.urls import path, include
from bar import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.menu, name=""),
    path("Меню", views.menu, name="Меню"),
    path("Выход", views.user_logout, name="Выход"),
    path("Добавить", views.add_item, name="Добавить"),
    path("Сохранить", views.save_item, name="Сохранить"),
    path("Смотреть/<int:item_id>", views.edit_item, name="Смотреть"),
    path("Обновить/<int:item_id>", views.update_item, name="Обновить"),
    path("Изменить доступность/<int:item_id>/<str:status>", views.change_status, name="Изменить доступность")

]

"""if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)"""
