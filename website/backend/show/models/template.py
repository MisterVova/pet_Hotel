from django.db import models
from django.template import Template as TemplateRender, Context, RequestContext
from django.utils.safestring import mark_safe


class Template(models.Model):
    destiny = models.CharField(verbose_name="Предназначение", max_length=64)
    title = models.CharField(verbose_name="Заголовок", max_length=64)
    description = models.TextField(verbose_name="Описание", null=True)
    template = models.TextField(verbose_name="HTML Шаблон", blank="", null=True)
    slug = models.SlugField(max_length=150, verbose_name='ЧПУ', blank=True, default='', db_index=True, unique=True)

    def __str__(self):
        return f"{self.destiny} | {self.title}"

    # def get_html(self, obj=None):
    #     print(F"+++++++++++++get_html++++++++++++ {obj}")
    #     # return f'asa'
    #     return f'<h5>:{self.title}:</h5>'
    #     # return f'{abc}'
    # from django.views.decorators.csrf import csrf_protect

    # @csrf_protect
    def render_to_html(self, obj=None, other=None):
        # # block_html = ""
        # try:
        #     layout = self.template
        #     print("layout+" , layout)
        #     template = Template(layout)
        #     render_context = Context({"object": context})
        #     block_html = template.render(render_context)
        # except Exception:
        #     block_html = ""
        #     print("Exception")
        #     # pass

        context = {
            "object": obj,
            "other": other,
        }

        layout = self.template
        # print("layout+", layout)
        template = TemplateRender(layout)

        # render_context = RequestContext(context)
        render_context = Context(context)
        # print("context+", render_context)
        block_html = template.render(render_context)

        return block_html
        # return mark_safe(block_html)

    class Meta:
        ordering = ('destiny', 'title')
        verbose_name = 'Шаблон'
        verbose_name_plural = 'Шаблоны'
