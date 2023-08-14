from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated

from rest_framework.viewsets import ModelViewSet

from garage.models import Accessory, Brand, Category, Car, Color
from garage.serializers import AccessorySerializer, BrandSerializer, CategorySerializer, CarSerializer, ColorSerializer, CarDetailSerializer, CarListSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]