# Generated by Django 4.1.7 on 2023-03-02 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0002_alter_itemcard_extras'),
    ]

    operations = [
        migrations.AddField(
            model_name='extras',
            name='list_number',
            field=models.IntegerField(default=1, verbose_name='Номер в списке ингредиентов'),
        ),
    ]
