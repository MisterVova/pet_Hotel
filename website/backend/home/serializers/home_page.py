from rest_framework import serializers

# from show.serializers import TemplateSerializer
from .reason import ReasonSerializer
from ..models import HomePage


class HomePageSerializer(serializers.ModelSerializer):
    # html_template = TemplateSerializer()
    reason = ReasonSerializer(many=True)

    class Meta:
        model = HomePage
        fields = "__all__"
