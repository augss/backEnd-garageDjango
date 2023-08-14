from rest_framework.serializers import ModelSerializer

from garage.models import Accessory, Brand, Category, Car, Color

class BrandSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"