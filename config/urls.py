from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

from uploader.router import router as uploader_router

from rest_framework.routers import DefaultRouter

from garage.views import AccessoryViewSet, BrandViewSet, CarViewSet, ColorViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r"accessories", AccessoryViewSet)
router.register(r"brands", BrandViewSet)
router.register(r"cars", CarViewSet)
router.register(r"colors", ColorViewSet)
router.register(r"categories", CategoryViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("api/media/", include(uploader_router.urls)),

]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
