from django.db import models

class Accessory(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name = "Accessory"
        verbose_name_plural = "Accessories"

class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name.upper()
    
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

class Color(models.Model):
    description = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name = "Color"
        verbose_name_plural = "Colors"

class Car(models.Model):
    model = models.CharField(max_length=50)
    year = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name="cars")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="cars")
    color = models.ForeignKey(Color, on_delete=models.PROTECT, related_name="cars")
    accessories = models.ManyToManyField(Accessory, related_name="cars")
    
    def __str__(self):
        return f"{self.model} {self.category} {self.color} {self.year}"
    
    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"


