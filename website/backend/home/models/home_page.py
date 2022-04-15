import django.http
from django.db import models
from garpix_page.models import BasePage
# from show.models.template import Template
from show.models import Template
from .reason import Reason
from django.http import HttpRequest

from garpix_notify.models import Notify
from django.conf import settings


class HomePage(BasePage):
    heading = models.TextField(verbose_name="Заголовок", null=False)
    description = models.TextField(verbose_name="Описание", null=True)
    html_template = models.ForeignKey(Template, verbose_name="html_template", related_name="template_HomePage",
                                      on_delete=models.PROTECT)
    reason = models.ManyToManyField(Reason, verbose_name="Reason", related_name="reasons_HomePage")
    template = "pages/home.html"

    def get_serializer(self):
        from ..serializers import HomePageSerializer
        return HomePageSerializer

    def get_context(self, request: HttpRequest = None, *args, **kwargs):
        from home.forms.BookingForm import BookingModelForm, BookingFormForm

        context = super().get_context(request, *args, **kwargs)
        message=""
        if request.method == "POST":
            form = BookingModelForm(request.POST)
            print(form.data)
            print(form.is_valid())
            if form.is_valid():
                booking = form.save(commit=False)
                booking.save()

                Notify.send(settings.BOOKING_EVENT, {
                    'booking': booking,
                }, email=booking.email)
                message='Бронирование гостиницы успешно отправлено'
        else:
            form = BookingModelForm()
        from django.middleware.csrf import get_token
        csrf_token = get_token(request)
        # csrf_token_html = '<input type="hidden" name="csrfmiddlewaretoken" value="{}" />'.format(csrf_token)

        # print(request.get_raw_uri())
        other = {
            # "other": Tag.objects.values()
            "other": {
                # "test": f"test {self.heading}",
                "form_hotel_booking": form,
                # "csrf_token_html" : csrf_token_html,
                "csrf_token": csrf_token,
                'message': message,
                # "form_hotel_booking_data": form.data,
            }

        }
        # global_c = context.get("global")
        # print("global_c==", type(global_c), global_c)

        context.update(other)
        return context

    class Meta:
        verbose_name = "HomePage"
        verbose_name_plural = "HomePages"
        ordering = ("-created_at",)
