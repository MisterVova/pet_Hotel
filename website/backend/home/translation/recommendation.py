from modeltranslation.translator import TranslationOptions, register
from ..models import Recommendation


@register(Recommendation)
class RecommendationTranslationOptions(TranslationOptions):
    pass
