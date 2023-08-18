# Generated by Django 4.2.2 on 2023-08-18 11:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("uploader", "0001_initial"),
        ("garage", "0010_car_accessories"),
    ]

    operations = [
        migrations.AddField(
            model_name="car",
            name="image",
            field=models.ManyToManyField(
                blank=True,
                default=None,
                null=True,
                related_name="+",
                to="uploader.image",
            ),
        ),
    ]
