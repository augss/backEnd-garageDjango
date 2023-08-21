from django.db import models

from garage.models import Category, Brand

class Model(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="models")
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name="models")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Model"
        verbose_name_plural = "Models"