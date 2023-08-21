# Generated by Django 4.2.2 on 2023-08-21 11:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("garage", "0003_remove_car_accessories"),
    ]

    operations = [
        migrations.AddField(
            model_name="car",
            name="accessories",
            field=models.ManyToManyField(related_name="cars", to="garage.accessory"),
        ),
    ]
