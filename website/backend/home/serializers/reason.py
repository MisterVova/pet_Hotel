from rest_framework import serializers
from ..models import Reason
from .recommendation import RecommendationSerializer


class ReasonSerializer(serializers.ModelSerializer):
    recommendations = RecommendationSerializer(many=True)

    class Meta:
        model = Reason
        fields = "__all__"
