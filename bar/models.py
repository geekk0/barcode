from django.db import models


class Extras(models.Model):
    name = models.CharField(verbose_name="Название", default="Название не указано", max_length=256)
    list_number = models.IntegerField(verbose_name="Номер в списке ингредиентов", default=1)

    def __str__(self):
        return self.name


class ItemCard(models.Model):
    name = models.CharField(verbose_name="Название", default="Название не указано", max_length=256)
    ingredients = models.TextField(verbose_name="Состав")
    volume = models.CharField(verbose_name="Объем", default="Объем не указан", max_length=256)
    photo = models.ImageField(verbose_name="Фото")
    extras = models.ManyToManyField(Extras, verbose_name="Дополнительные ингредиенты", blank=True)
    available = models.BooleanField(verbose_name="Доступен к заказу", default=True)

    def __str__(self):
        return self.name


