from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated

from rest_framework.viewsets import ModelViewSet

from garage.models import Accessory, Brand, Category, Car, Color
from garage.serializers import AccessorySerializer, BrandSerializer, CategorySerializer, CarSerializer, ColorSerializer, CarDetailSerializer, CarListSerializer

class BrandViewSet(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [IsAuthenticated]