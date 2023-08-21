from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from garage.models import Model
from garage.serializers import ModelSerializer

class ModelViewSet(ModelViewSet):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer