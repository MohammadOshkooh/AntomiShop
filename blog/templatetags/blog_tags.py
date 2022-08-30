from django import template

register = template.Library()


@register.simple_tag
def get_n_last_records(objects, n):
    if objects is not None:
        if objects.count() >= n:
            return objects[:n]
        else:
            return objects
