# Generated by Django 4.2.2 on 2023-08-18 11:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("uploader", "0001_initial"),
        ("garage", "0011_car_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="image",
            field=models.ManyToManyField(related_name="+", to="uploader.image"),
        ),
    ]