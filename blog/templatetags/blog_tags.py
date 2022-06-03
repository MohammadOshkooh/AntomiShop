from django import template

register = template.Library()


# @register.simple_tag
# def is_child(self, parent):
#     """
#     return: self is_child parent
#     """
#     while self.parent is not None:
#         if self.parent == parent:
#             return True
#         else:
#             self = self.parent
#     return False

@register.simple_tag
def get_n_last_records(objects, n):
    return objects.order_by('-id')[:n]
