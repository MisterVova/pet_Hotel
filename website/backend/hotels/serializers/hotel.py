from rest_framework import serializers

from .housing_type import HousingTypeSerializer
from .infrastructure import InfrastructureSerializer
from ..models import Hotel


class HotelSerializer(serializers.ModelSerializer):

    housing_type = HousingTypeSerializer
    infrastructure = InfrastructureSerializer

    class Meta:
        model = Hotel
        fields = "__all__"
