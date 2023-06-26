from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name.UPPER()
    
    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"
    
class Category(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Acessory(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name = "Acessory"
        verbose_name_plural = "Acessories"

class Car(models.Model):
    model = models.CharField(max_length=50)
    year = models.IntegerField(null=True, blank=True)
    color = models.CharField(max_length=50, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name="cars")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="cars")
    
    def __str__(self):
        return f"{self.brand} {self.model} {self.color} {self.year}"
    
    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"

