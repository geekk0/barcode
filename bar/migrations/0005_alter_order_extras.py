# Generated by Django 4.1.7 on 2023-03-03 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0004_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='extras',
            field=models.ManyToManyField(blank=True, related_name='selected_extras', to='bar.extras', verbose_name='Выбранные допы'),
        ),
    ]
