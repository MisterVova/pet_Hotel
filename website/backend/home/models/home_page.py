from django.db import models
from garpix_page.models import BasePage
# from show.models.template import Template
from show.models import Template
from .reason import Reason


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

    def get_context(self, request=None, *args, **kwargs):
        # from ..models import Reason

        context = super().get_context(request, *args, **kwargs)
        all_tags = {
            # "all_tags": Tag.objects.values()
            "test": {"test": f"test {self.heading}"}

        }
        # global_c = context.get("global")
        # print("global_c==", type(global_c), global_c)

        context.update(all_tags)
        return context

    class Meta:
        verbose_name = "HomePage"
        verbose_name_plural = "HomePages"
        ordering = ("-created_at",)
