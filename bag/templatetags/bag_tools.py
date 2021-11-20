from django import template


register = template.Library()


@register.filter(name='calc_total')
def calc_total(product_price, line_qty):
    return product_price * line_qty
