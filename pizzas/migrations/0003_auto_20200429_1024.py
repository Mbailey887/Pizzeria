# Generated by Django 3.0.5 on 2020-04-29 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0002_topping'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pizza',
            new_name='PizzaName',
        ),
        migrations.RenameField(
            model_name='topping',
            old_name='pizza',
            new_name='pizzaname',
        ),
    ]
