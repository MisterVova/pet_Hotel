from ..models import BookingForm
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(BookingForm)
class BookingFormAdmin(admin.ModelAdmin):
    pass
