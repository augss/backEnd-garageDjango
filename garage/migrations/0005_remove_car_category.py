# Generated by Django 4.2.2 on 2023-08-21 11:50

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("garage", "0004_car_accessories"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="car",
            name="category",
        ),
    ]