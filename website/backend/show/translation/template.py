from modeltranslation.translator import TranslationOptions, register
from ..models import Template


@register(Template)
class TemplateTranslationOptions(TranslationOptions):
    pass
