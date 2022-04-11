from modeltranslation.translator import TranslationOptions, register
from ..models import HomePage


@register(HomePage)
class HomePageTranslationOptions(TranslationOptions):
    pass
