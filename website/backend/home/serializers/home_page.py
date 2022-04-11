from rest_framework import serializers

from show.serializers import TemplateSerializer
from .reason import ReasonSerializer
from ..models import HomePage


class HomePageSerializer(serializers.ModelSerializer):
    blocks = TemplateSerializer(many=True)
    reason = ReasonSerializer(many=True)

    class Meta:
        model = HomePage
        fields = "__all__"
