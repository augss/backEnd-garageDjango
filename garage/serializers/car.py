from rest_framework.serializers import ModelSerializer, SlugRelatedField

from uploader.models import Image
from uploader.serializers import ImageSerializer


from garage.models import Car

class CarSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"

    image_attachment_key = SlugRelatedField(
        source="image",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True
    )
    image = ImageSerializer(required=False, read_only=True)


class CarDetailSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"
        depth = 1


class CarListSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = ["id", "price"]

