from ..models import Hotel
from django.contrib import admin


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    pass
