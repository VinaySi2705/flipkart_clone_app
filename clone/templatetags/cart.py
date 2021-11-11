from django import template
from clone.models import Customer
register = template.Library()


@register.filter(name='is_in_cart')
def is_in_cart(product, cart):
    keys = cart.keys()
    # print("keys=>",keys)
    for id in keys:
        if int(id) == product.id:
            return True
    return False


@register.filter(name='cart_quantity')
def cart_quantity(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return 0


@register.filter(name='price_total')
def price_total(product, cart):
    return product.price*cart_quantity(product, cart)


@register.filter(name='total_cart_price')
def total_cart_price(products, cart):
    sum = 0
    for p in products:
        sum += price_total(p, cart)
    return sum


@register.filter(name='order_price')
def order_price(order):
    return order.quantity*order.price


@register.filter(name='profile')
def profile(customer_id):
    nameobject = Customer.objects.filter(id=customer_id)
    return nameobject
