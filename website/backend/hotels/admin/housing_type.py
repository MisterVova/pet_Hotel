from ..models import HousingType
from django.contrib import admin


@admin.register(HousingType)
class HousingTypeAdmin(admin.ModelAdmin):
    pass
