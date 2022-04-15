import random

from django.core.paginator import Page
from django.db import models
from django.http import HttpRequest
from garpix_page.models import BasePage
from garpix_utils.paginator import GarpixPaginator

from hotels.models.hotel import Hotel, HousingTypeTextChoices
from show.models import Template


class HotelsPage(BasePage):
    paginate_by = 5
    template = "pages/hotels.html"
    heading = models.TextField(verbose_name="Заголовок", null=False)
    description = models.TextField(verbose_name="Описание", null=True)
    html_template = models.ForeignKey(Template, verbose_name="html_template", related_name="template_HotelsPage",
                                      on_delete=models.PROTECT)

    def get_serializer(self):
        from ..serializers import HotelsPageSerializer
        return HotelsPageSerializer

    def get_context_old(self, request: HttpRequest = None, *args, **kwargs):
        # from ..forms.filter_hotels import FilterHotelsForm
        from . import Hotel
        context = super().get_context(request, *args, **kwargs)

        # hotels = Hotel.objects.all()
        hotels = Hotel.objects.values()

        # hotels
        hotels = list(hotels)[0:3]
        # print("hotels+=1=", hotels)

        # print("hotels+=2=",hotels[1:3])
        all_tags = {
            # "all_tags": Tag.objects.values()
            "test": f"test {self.heading}"
        }

        context.update(all_tags)
        from django.core import serializers

        obj = context.get("object")
        # obj = self.get_serializer()(context.get("object"))
        # obj = self.get_serializer()(context.get("object"))
        # obj = serializers.serialize("json", obj, )
        # obj = dict(obj)

        from hotels.serializers import HotelsPageSerializer
        my_context = {
            "context": {
                "tesst": "dasdada",
                "object": obj.id,
                # "object": obj.get_serializer()(obj).data,
                # "object": HotelsPageSerializer(obj).data,
                "hotels": hotels,
            }
        }

        # print("obj==", type(obj), obj)
        # obj["hotels"] = hotels
        # obj = {
        #     # "object":{ "hotels":hotels.values() }
        #     "object": {"hotels": hotels}
        # }
        context.update(my_context)

        print("request=", request)
        if request == None:
            return context
        # forms = {
        #     # "all_tags": Tag.objects.values()
        #     "forms": FilterHotelsForm().values()
        # }
        # context.update(forms)

        # if request.method == "GET":
        #     forms = FilterHotelsForm(request.GET)
        #     print("forms=\n", forms)
        #     if forms.is_valid():
        #         print("forms=ok", forms)

        if 'apartments' in request.GET:
            print("apartments=", request.GET['apartments'])
            # message = 'You searched for: %r' % request.GET['q']
        else:
            print("apartments=", "'You submitted an empty forms.'")
            # message = 'You submitted an empty forms.'

        return context

    def get_context(self, request: HttpRequest = None, *args, **kwargs):
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print("args")
        print(args)
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print("kwargs")
        print(kwargs)
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print("request.GET")
        print(request.GET)
        query_dict = {}
        if request.method == "GET":
            query_dict = request.GET.dict()

        # if "page" in query_dict.keys():
        #     query_dict_len = 1

        if (len(query_dict) == 0):
            from hotels.forms.default import query_dict_default
            query_dict = query_dict_default

        hotels = Hotel.get_hotels_by_query(query_dict)
        # if 'apartments' in request.GET:
        #     query_dict = request.GET.copy()
        #     print("apartments=", request.GET['apartments'])
        #     # message = 'You searched for: %r' % request.GET['q']
        # else:
        #     print("apartments=", "'You submitted an empty forms.'")
        #     # message = 'You submitted an empty forms.'

        from garpix_utils.paginator import GarpixPaginator
        paginator = GarpixPaginator(hotels, self.paginate_by)

        # print("page_range_beauty", paginator.page_range_beauty, )

        try:
            page = int(query_dict.get("page", 1))
            # page = int(request.GET.get("page", 1))
        except ValueError:
            page = 1

        paginator_hotels = paginator.get_page(page)

        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

        context = super().get_context(request, *args, **kwargs)

        from django.middleware.csrf import get_token
        csrf_token = get_token(request)

        # print(request.get_raw_uri())
        from hotels.serializers import HotelSerializer
        hs = HotelSerializer(paginator_hotels, many=True).data
        other = {
            # "other": Tag.objects.values()
            "other": {
                "csrf_token": csrf_token,
                "query_dict": query_dict,
                "hotels": hs,
                "paginator": self.get_paginator_dict(paginator_hotels, paginator),
                # "paginator": paginator,
                # 'message': message,
                # "form_hotel_booking_data": form.data,
            }

        }
        # global_c = context.get("global")
        # print("global_c==", type(global_c), global_c)

        context.update(other)
        # addd()

        return context

    class Meta:
        verbose_name = "HotelsPage"
        verbose_name_plural = "HotelsPages"
        ordering = ("-created_at",)

    @staticmethod
    def get_paginator_dict(page: Page, paginator: GarpixPaginator):
        ret_dict = {
            "page_range_beauty": paginator.page_range_beauty,
            "count": paginator.count,  # число элементов в списке
            "num_pages": paginator.num_pages,  # число страниц (10:3 = 4 – округление до большего)
            "page_number": page.number,  # номер следующей страницы
            # "page_range": paginator.page_range,  # итератор для перебора номеров страниц
            # "object_list": page.object_list,  # список элементов текущей страницы
            "has_next": page.has_next(),  # имеется ли следующая страница
            "has_previous": page.has_previous(),  # имеется ли предыдущая страница
            "has_other_pages": page.has_other_pages(),  # имеются ли вообще страницы
            # "next_page_number": page.next_page_number(),  # номер следующей страницы
            # "previous_page_number": page.previous_page_number(),  # номер предыдущей страницы
        }
        if page.has_next():
            ret_dict["next_page_number"] = page.next_page_number()
        if page.has_previous():
            ret_dict["previous_page_number"] = page.previous_page_number()
        return ret_dict


def addd():
    random.seed()
    for x in range(10):
        n = x + 11
        h = Hotel(
            name=f"AMARA STAR {n}",
            text=f"Гостиница у подножия красных скал во время заката AMARA STAR {n}",
            image=None,
            rating=random.randint(1, 9) + random.randint(0, 9) % 10,  # случайное целое число N, A ≤ N ≤ B.,
            min_price=random.randint(1, 9) * 1000,
            max_price=random.randint(1, 9) * 10000,
            star=random.randint(1, 5),
            has_wifi=True if random.randint(0, 1) == 1 else False,
            has_pool=True if random.randint(0, 1) == 1 else False,
            has_parking=True if random.randint(0, 1) == 1 else False,
            # housing_type=f"",
            housing_type_text_choices=HousingTypeTextChoices.HOTEL,
            # infrastructure=f"",
            slug=f"AMARA_STAR_{n}",
        )
        h.save()
