from rest_framework import serializers

from ..models import HotelsPage
from show.serializers import TemplateSerializer


class HotelsPageSerializer(serializers.ModelSerializer):
    blocks = TemplateSerializer(many=True)

    class Meta:
        model = HotelsPage
        fields = "__all__"
