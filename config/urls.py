from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

from uploader.router import router as uploader_router

from user.router import router as user_router


from rest_framework.routers import DefaultRouter

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from garage.views import AccessoryViewSet, BrandViewSet, ModelViewSet, CarViewSet, ColorViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r"accessories", AccessoryViewSet)
router.register(r"brands", BrandViewSet)
router.register(r"cars", CarViewSet)
router.register(r"colors", ColorViewSet)
router.register(r"categories", CategoryViewSet)
router.register(r"models", ModelViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/media/", include(uploader_router.urls)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path("api/", include(user_router.urls)),
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
