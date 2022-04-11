from ..models import Infrastructure
from django.contrib import admin


@admin.register(Infrastructure)
class InfrastructureAdmin(admin.ModelAdmin):
    pass
