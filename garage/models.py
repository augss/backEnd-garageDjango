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