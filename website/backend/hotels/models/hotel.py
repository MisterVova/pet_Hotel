from django.db import models
from django.http import HttpRequest, QueryDict

from garpix_utils.file import get_file_path

from hotels.models.housing_type import HousingType
from hotels.models.infrastructure import Infrastructure


class HousingTypeTextChoices(models.TextChoices):
    HOTEL = "Hotel", "Гостиница"
    MOTEL = "Motel", "Мотель"
    APARTMENT = "Apartment", "Апартамент"
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
    housing_type = models.ForeignKey(HousingType, verbose_name="тип жилья", on_delete=models.SET_NULL, related_name='housing_type_hotel2', null=True, )
    housing_type_text_choices = models.CharField(verbose_name="тип жилья", max_length=16, null=True, choices=HousingTypeTextChoices.choices, blank=True, )
    infrastructure = models.ManyToManyField(Infrastructure, verbose_name="инфраструктура", related_name='housing_type_infrastructure', blank=True)
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

    @staticmethod
    def get_hotels_by_query(query_dict: QueryDict = None):
        # query_dict_default = {
        #     "pool": "on",
        #     # "parking": "on",
        #     # "wi_fi": "on",
        #     "hotel": "on",
        #     "motel": "on",
        #     "apartments": "on",
        #     # "min_price": "0",
        #     # "max_price": "3000",
        #     "ordering": "+name",
        #     # "ordering": "+price",
        #     "page": 1,
        # }

        ordering = "+name"
        if "ordering" in query_dict.keys():
            ordering = str(query_dict["ordering"])
        if ordering[0] == "+": ordering = ordering[1:]
        # print("ordering",ordering)

        has_wifi = True if "wi_fi" in query_dict.keys() else False
        has_pool = True if "pool" in query_dict.keys() else False
        has_parking = True if "parking" in query_dict.keys() else False
        hotel = True if "hotel" in query_dict.keys() else False
        motel = True if "motel" in query_dict.keys() else False
        apartments = True if "apartments" in query_dict.keys() else False

        has_min_price = True if "min_price" in query_dict.keys() else False
        has_max_price = True if "max_price" in query_dict.keys() else False

        try:
            min_value = int(query_dict.get("min_price", ""))
        except ValueError:
            min_value = None

        try:
            max_value = int(query_dict.get("max_price", ""))
        except ValueError:
            max_value = None

        if not min_value: has_min_price = False
        if not max_value: has_max_price = False


        if has_min_price & has_max_price:
            min_value , max_value = min(min_value , max_value), max(min_value , max_value)


        print(
            has_wifi,
            has_pool,
            has_parking,
            hotel,
            motel,
            apartments,

            min_value,
            max_value,
            
            has_min_price,
            has_max_price,
        )

        from django.db.models import Q
        q_has_wifi = Q(has_wifi__exact=has_wifi)
        q_has_pool = Q(has_pool__exact=has_pool)
        q_has_parking = Q(has_parking__exact=has_parking)

        q_hotel = Q(housing_type_text_choices__exact=HousingTypeTextChoices.HOTEL)
        q_motel = Q(housing_type_text_choices__exact=HousingTypeTextChoices.MOTEL)
        q_apartments = Q(housing_type_text_choices__exact=HousingTypeTextChoices.APARTMENT)

        q_min_price = Q(min_price__gte=min_value)
        q_max_price = Q(min_price__lte=max_value)


        q_and = Q()
        if has_wifi: q_and = q_and & q_has_wifi
        if has_pool: q_and = q_and & q_has_pool
        if has_parking: q_and = q_and & q_has_parking

        q_or = Q()
        if hotel: q_or = q_or | q_hotel
        if motel: q_or = q_or | q_motel
        if apartments: q_or = q_or | q_apartments

        q_price = Q()
        if has_min_price: q_price = q_price & q_min_price
        if has_max_price: q_price = q_price & q_max_price

        q_s = q_or & q_and  & q_price

        print(
            Q(),
            "====q_and",
            q_and,
            "====q_or",
            q_or,
            "====q_price",
            q_price,
            "====q_s",
            q_s,
            "====",

            # q_has_wifi,
            # q_has_pool,
            # q_has_parking,
            # q_hotel,
            # q_motel,
            # q_apartments,
            # q_min_price,
            # q_max_price,
            sep="\n"
        )

        # print( "q_price=",  q_price,"ordering", ordering,sep="\n")
        # ret = Hotel.objects.filter(q_price).order_by(ordering)

        # print("q_or=", q_or, "ordering", ordering, sep="\n")
        # ret = Hotel.objects.filter(q_or).order_by(ordering)

        # print("q_and=", q_and, "ordering", ordering, sep="\n")
        # ret = Hotel.objects.filter(q_and).order_by(ordering)

        print("q_s=", q_s, "ordering", ordering, sep="\n")
        ret = Hotel.objects.filter(q_s).order_by(ordering)
        # ret = Hotel.objects.all().order_by(ordering)
        return ret
