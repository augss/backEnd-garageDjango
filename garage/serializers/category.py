from rest_framework.serializers import ModelSerializer

from garage.models import Accessory, Brand, Category, Car, Color

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
