from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from garage.views import AccessoryViewSet, BrandViewSet, CarViewSet, ColorViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r"accessory", AccessoryViewSet)
router.register(r"brand", BrandViewSet)
router.register(r"car", CarViewSet)
router.register(r"color", ColorViewSet)
router.register(r"category", CategoryViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
