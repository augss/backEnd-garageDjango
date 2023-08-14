from rest_framework.serializers import ModelSerializer

from garage.models import Accessory, Brand, Category, Car, Color

class ColorSerializer(ModelSerializer):
    class Meta:
        model = Color
        fields = "__all__"