from rest_framework.serializers import ModelSerializer

from garage.models import Accessory, Brand, Category, Car, Color

class CarSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"

class CarDetailSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"
        depth = 1


class CarListSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = ["id", "brand", "price"]
