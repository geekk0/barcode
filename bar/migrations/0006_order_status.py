# Generated by Django 4.1.7 on 2023-03-04 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0005_alter_order_extras'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Активный заказ'),
        ),
    ]
