
from django.db import models

from uploader.models import Image

from . import Brand, Category, Color, Accessory

class Car(models.Model):
    model = models.CharField(max_length=50)
    year = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name="cars")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="cars")
    color = models.ForeignKey(Color, on_delete=models.PROTECT, related_name="cars")
    accessories = models.ManyToManyField(Accessory, related_name="cars")
    image = models.ManyToManyField(
        Image,
        related_name="+",
    )
    
    def __str__(self):
        return f"{self.model} {self.category} {self.color} {self.year}"
    
    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"