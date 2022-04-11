from ..models.hotels_page import HotelsPage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(HotelsPage)
class HotelsPageAdmin(BasePageAdmin):
    pass
