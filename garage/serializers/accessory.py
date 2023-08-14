from rest_framework.serializers import ModelSerializer

from garage.models import Accessory, Brand, Category, Car, Color

class AccessorySerializer(ModelSerializer):
    class Meta:
        model = Accessory
        fields = "__all__"
