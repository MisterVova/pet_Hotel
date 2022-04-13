from django.db import models
from django.http import HttpRequest
from garpix_page.models import BasePage
from show.models import Template


class HotelsPage(BasePage):
    template = "pages/hotels.html"
    heading = models.TextField(verbose_name="Заголовок", null=False)
    description = models.TextField(verbose_name="Описание", null=True)
    html_template = models.ForeignKey(Template, verbose_name="html_template", related_name="template_HotelsPage",
                                      on_delete=models.PROTECT)

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

    class Meta:
        verbose_name = "HotelsPage"
        verbose_name_plural = "HotelsPages"
        ordering = ("-created_at",)
