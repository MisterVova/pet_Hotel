from django.db import models

from garpix_utils.file import get_file_path

from hotels.models.housing_type import HousingType
from hotels.models.infrastructure import Infrastructure


class HousingTypeTextChoices(models.TextChoices):
    PC = "Hotel", "Гостиница"
    LAPTOP = "Motel", "Мотель"
    PRINTER = "Apartment", "Апартамент"
    __empty__ = "Выберите тип жилья"


class Hotel(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=64)
    text = models.TextField(verbose_name='Текст', blank=True, null=True)
    image = models.ImageField(verbose_name="Картинка", blank=True, null=True, upload_to=get_file_path)

    rating = models.FloatField(verbose_name='rating', blank=True, null=True)
    min_price = models.FloatField(verbose_name='Цена от', blank=True, null=True)
    max_price = models.FloatField(verbose_name='Цена до', blank=True, null=True)
    star = models.SmallIntegerField(verbose_name='star', blank=True, null=True)

    has_wifi = models.BooleanField(verbose_name="wifi", default=False)
    has_pool = models.BooleanField(verbose_name="pool", default=False)
    has_parking = models.BooleanField(verbose_name="parking", default=False)

    housing_type = models.ForeignKey(HousingType, verbose_name="тип жилья", on_delete=models.SET_NULL,
                                     related_name='housing_type_hotel2',null=True,)

    housing_type_text_choices = models.CharField(verbose_name="тип жилья", max_length=16, null=True,
                                                 choices=HousingTypeTextChoices.choices, blank=True, )

    infrastructure = models.ManyToManyField(Infrastructure, verbose_name="инфраструктура",
                                            related_name='housing_type_infrastructure', blank=True)

    slug = models.SlugField(max_length=150, verbose_name='ЧПУ', unique=True, blank=True, default='', db_index=True)

    def __str__(self):
        return f"{self.name} | {self.housing_type}"

    def get_serializer(self):
        from ..serializers import HotelSerializer
        return HotelSerializer

    class Meta:
        ordering = ('name',)
        verbose_name = 'Гостиница'
        verbose_name_plural = 'Гостиницы'
