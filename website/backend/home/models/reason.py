from django.db import models

from home.models.recommendation import Recommendation
from garpix_utils.file import get_file_path


class Reason(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=64)
    text = models.TextField(verbose_name='Текст')
    image = models.ImageField(verbose_name="Картинка", blank=True, null=True, upload_to=get_file_path)
    recommendations = models.ManyToManyField(Recommendation, verbose_name="Рекомендации", related_name="reasons",
                                             blank=True,)

    def __str__(self):
        return f"{self.title} | {self.text}"

    class Meta:
        ordering = ('title',)
        verbose_name = 'Причина'
        verbose_name_plural = 'Причины'
