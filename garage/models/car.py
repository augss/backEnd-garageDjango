
from django.db import models

from uploader.models import Image

from . import Category, Color, Model, Accessory

class Car(models.Model):
    model = models.ForeignKey(Model, on_delete=models.PROTECT, related_name="cars")
    year = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, blank=True)
    color = models.ForeignKey(Color, on_delete=models.PROTECT, related_name="cars")
    image = models.ManyToManyField(
        Image,
        related_name="+",
    )
    accessories = models.ManyToManyField(Accessory, related_name="cars")
    
    def __str__(self):
        return f"{self.model} {self.color} {self.year}"
    
    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"