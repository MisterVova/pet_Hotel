from rest_framework import serializers

from ..models.hotels_page import HotelsPage
# from show.serializers import TemplateSerializer


class HotelsPageSerializer(serializers.ModelSerializer):
    # html_template = TemplateSerializer()

    class Meta:
        model = HotelsPage
        fields = "__all__"
