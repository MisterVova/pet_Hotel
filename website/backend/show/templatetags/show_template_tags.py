from django import template

register = template.Library()


# template
# @register.simple_tag(name="render_template_to_html")
# def template_render_to_html(blocks, context):
#     ret = ""
#     for block in blocks:
#         ret += f"\n {block.render_to_html(context)}"
#         # try:
#         #     ret += f" {block.render_to_html(context)}"
#         # except Exception:
#         #     pass
#
#     return ret
#
#     # return f"render::{block.render_to_html(context)}::render"


@register.simple_tag(name="render_html")
def template_render_to_html(template, obj=None, other=None, csrf_token_html=None):
    # context = {
    #     "object": obj,
    #     "other": other,
    # }
    return template.render_to_html(obj, other, csrf_token_html)
    # return f"render::{template.render_to_html(obj,other)}::render"


@register.simple_tag(name="my_tag_test")
def template_test(p1=None, p2=None, p3=None):
    return f"""<h5>::blocks_test::</h5><br>
            p1={p1}<br>p2={p2}<br>p3={p3}
           """

#
# @register.simple_tag(name="all_context_render_to_html")
# def all_context_render_to_html(templates, context):
#     ret = ""
#     for template in templates:
#         ret += f"\n {template.render_to_html(context)}"
#         # try:
#         #     ret += f" {template.render_to_html(context)}"
#         # except Exception:
#         #     pass
#
#     return ret
