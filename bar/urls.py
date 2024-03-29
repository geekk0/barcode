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
    path("Изменить доступность/<int:item_id>/<str:status>", views.change_status, name="Изменить доступность"),
    path("Удалить/<int:item_id>", views.delete_item, name="Удалить"),
    # path("Фильтровать заказы", views.orders_filter, name="Фильтровать заказы"),
    path("Заказы", views.orders_list, name="Заказы"),
    path("Заказ выполнен/<int:order_id>", views.order_completed, name="Заказ выполнен"),
    path("Удалить заказ/<int:order_id>", views.delete_order, name="Удалить заказ"),

]

"""if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)"""
