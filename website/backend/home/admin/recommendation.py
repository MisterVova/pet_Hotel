from ..models import Recommendation
from django.contrib import admin


@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    pass
