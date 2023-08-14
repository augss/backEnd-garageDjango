from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name.upper()
    
    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"