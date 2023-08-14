from django.db import models
    
class Color(models.Model):
    description = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name = "Color"
        verbose_name_plural = "Colors"