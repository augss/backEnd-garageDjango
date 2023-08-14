from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated

from rest_framework.viewsets import ModelViewSet

from garage.models import Accessory, Brand, Category, Car, Color
from garage.serializers import AccessorySerializer, BrandSerializer, CategorySerializer, CarSerializer, ColorSerializer, CarDetailSerializer, CarListSerializer

class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return CarListSerializer
        elif self.action == "retrieve":
            return CarDetailSerializer
        return CarSerializer
    permission_classes = [IsAuthenticated]

