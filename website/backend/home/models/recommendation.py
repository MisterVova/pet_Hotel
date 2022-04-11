from django.db import models


class Recommendation(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=64)
    text = models.TextField(verbose_name='Текст')
    # background_image = models.TextField(verbose_name='Фоновое изображение')

    def __str__(self):
        return f"{self.title} | {self.text}"

    class Meta:
        ordering = ('title',)
        verbose_name = 'Рекомендация'
        verbose_name_plural = 'Рекомендации'
