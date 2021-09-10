from django import template

""" A function to calculate the subtotals in cart """
register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity
