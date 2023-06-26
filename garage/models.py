from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name.UPPER()
    
class Category(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description