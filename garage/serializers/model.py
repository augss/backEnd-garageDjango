from rest_framework.serializers import ModelSerializer

from garage.models import Model

class ModelSerializer(ModelSerializer):
    class Meta:
        model = Model
        fields = "__all__"