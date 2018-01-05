from django import template


register = template.Library()


@register.simple_tag
def make_star(level):
    stars = []
    for index, i in enumerate(range(11)):
        if index <= int(level):
            stars.append('<span class="fa fa-circle checked"></span>')
        else:
            stars.append('<span class="fa fa-circle"></span>')

    return ''.join(stars)
