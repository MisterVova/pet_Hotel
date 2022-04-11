from modeltranslation.translator import TranslationOptions, register
from ..models import HotelsPage


@register(HotelsPage)
class HotelsPageTranslationOptions(TranslationOptions):
    pass
