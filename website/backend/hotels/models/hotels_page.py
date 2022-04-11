from django.db import models
from django.http import HttpRequest
from garpix_page.models import BasePage
from blocks.models.block import Block


class HotelsPage(BasePage):
    template = "pages/hotels.html"
    heading = models.TextField(verbose_name="Заголовок", null=False)
    description = models.TextField(verbose_name="Описание", null=True)
    blocks = models.ManyToManyField(Block, verbose_name="Блоки", related_name="reasons_HotelsPage")

    def get_serializer(self):
        from ..serializers import HotelsPageSerializer
        return HotelsPageSerializer

    def get_context(self, request: HttpRequest = None, *args, **kwargs):
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

        # self.addvv("DSDS","Asdasda")

        obj = context.get("object")
        # obj = self.get_serializer()(context.get("object"))
        # obj = self.get_serializer()(context.get("object"))
        # obj = serializers.serialize("json", obj, )
        # obj = dict(obj)

        from hotels.serializers import HotelsPageSerializer
        my_context = {
            "context": {
                "tesst": "dasdada",
                # "object": obj.id,
                "object": obj.get_serializer()(obj).data,
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
        # form = {
        #     # "all_tags": Tag.objects.values()
        #     "form": FilterHotelsForm().values()
        # }
        # context.update(form)

        # if request.method == "GET":
        #     form = FilterHotelsForm(request.GET)
        #     print("form=\n", form)
        #     if form.is_valid():
        #         print("form=ok", form)

        if 'apartments' in request.GET:
            print("apartments=", request.GET['apartments'])
            # message = 'You searched for: %r' % request.GET['q']
        else:
            print("apartments=", "'You submitted an empty form.'")
            # message = 'You submitted an empty form.'

        return context

    class Meta:
        verbose_name = "HotelsPage"
        verbose_name_plural = "HotelsPages"
        ordering = ("-created_at",)
