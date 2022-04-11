from modeltranslation.translator import TranslationOptions, register
from ..models import Reason


@register(Reason)
class ReasonTranslationOptions(TranslationOptions):
    pass
