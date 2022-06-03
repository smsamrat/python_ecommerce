
from django import template
from App_order.models import Order
register = template.Library()

@register.filter
def cartTotal(user):
    order = Order.objects.filter(user=user, orderd=False)
    if order.exists():
       return order[0].orderItems.count()
    else:
       return 0 