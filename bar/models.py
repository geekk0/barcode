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


class Order(models.Model):
    time = models.DateTimeField(verbose_name="Дата время заказа")
    location = models.CharField(verbose_name="Куда принести", default="Локация не указана", max_length=256)
    item = models.ForeignKey(ItemCard, verbose_name="Блюда", on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name="Количество")
    sugar = models.IntegerField(verbose_name="Сахар")
    extras = models.ManyToManyField(Extras, verbose_name="Выбранные допы", blank=True, related_name="selected_extras")
    status = models.BooleanField(verbose_name="Активный заказ", default=True)

    def __str__(self):
        return str(self.id)



