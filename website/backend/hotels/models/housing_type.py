from django.db import models


class HousingType(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=64, unique=True, db_index=True)
    description = models.TextField(verbose_name="Описание", null=True)
    slug = models.SlugField(max_length=150, verbose_name='ЧПУ', unique=True, blank=True, default='', db_index=True)

    def __str__(self):
        return f"{self.name} "

    class Meta:
        ordering = ('name',)
        verbose_name = 'Тип жилья'
        verbose_name_plural = 'Типы жилья'
