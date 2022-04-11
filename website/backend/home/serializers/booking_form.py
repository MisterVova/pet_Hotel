from rest_framework import serializers
from ..models import BookingForm


class BookingFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingForm
        fields = "__all__"
