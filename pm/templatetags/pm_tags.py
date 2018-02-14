from django import template


register = template.Library()


@register.simple_tag
def minus(a, b):
    return a - b
