from modeltranslation.translator import TranslationOptions, register
from ..models import BookingForm


@register(BookingForm)
class BookingFormTranslationOptions(TranslationOptions):
    pass
