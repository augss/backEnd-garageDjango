from django.contrib import admin

from garage.models import Accessory, Brand, Category, Car, Color

admin.site.register(Accessory)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Car)
admin.site.register(Color)