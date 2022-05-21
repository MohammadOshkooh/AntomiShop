from django import template

register = template.Library()


@register.simple_tag
def subtract(x, y):
    return x - y

#
# @register.simple_tag
# def while_loop(x, y):
#     """
#
#       while(category.child != None):
#         {{category}}
#
#
#     """
