from ..models.home_page import HomePage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(HomePage)
class HomePageAdmin(BasePageAdmin):
    pass
