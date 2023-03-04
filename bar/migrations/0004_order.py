# Generated by Django 4.1.7 on 2023-03-03 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0003_extras_list_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='Дата время заказа')),
                ('location', models.CharField(default='Локация не указана', max_length=256, verbose_name='Куда принести')),
                ('quantity', models.IntegerField(verbose_name='Количество')),
                ('sugar', models.IntegerField(verbose_name='Сахар')),
                ('extras', models.ManyToManyField(blank=True, to='bar.extras', verbose_name='Выбранные допы')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bar.itemcard', verbose_name='Блюда')),
            ],
        ),
    ]
