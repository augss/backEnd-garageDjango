from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from garage.models import Accessory, Brand, Category, Car, Color
from garage.serializers import AccessorySerializer, BrandSerializer, CategorySerializer, CarSerializer, ColorSerializer

class AccessoryViewSet(ModelViewSet):
    queryset = Accessory.objects.all()
    serializer_class = AccessorySerializer

class BrandViewSet(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ColorViewSet(ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer

class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer