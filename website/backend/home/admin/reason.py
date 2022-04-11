from ..models import Reason
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(Reason)
class ReasonAdmin(admin.ModelAdmin):
    pass
