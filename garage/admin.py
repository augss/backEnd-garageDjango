from django.contrib import admin

from garage.models import Accessory, Brand, Category, Car

admin.site.register(Accessory)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Car)
