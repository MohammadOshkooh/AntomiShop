from django.template import Library

from shop.models import Product, ProductCategory

register = Library()


@register.simple_tag
def get_main_categories_products():
    categories = ProductCategory.objects.all()
    main_parents = []
    for c in categories:
        if c.parent is None:
            main_parents.append(c)
    return main_parents


@register.simple_tag
def order_by_discount():
    qs = Product.objects.filter(availability=True)
    unsorted_results = qs.all()
    sorted_results = sorted(unsorted_results, key=lambda t: t.get_discount(), reverse=True)
    return sorted_results
