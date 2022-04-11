from rest_framework import serializers
from ..models import HousingType


class HousingTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = HousingType
        fields = "__all__"