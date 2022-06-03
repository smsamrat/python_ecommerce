from django.shortcuts import render
from .forms import BillignsAddressForm
from .models import BillignsAddress
from App_order.models import Order

# Create your views here.

def checkOut(request):
    save_address = BillignsAddress.objects.get_or_create(user=request.user)[0]

    form = BillignsAddressForm(instance=save_address)
    if request.method == 'POST':
        form = BillignsAddressForm(request.POST,instance=save_address)
        if form.is_valid():
            form.save()
            form = BillignsAddressForm(instance=save_address)
    # order_item = Cart.objects.filter(user=request.user, purchased=False)#aivbae dia jai
    order_qs = Order.objects.filter(user=request.user, orderd=False)
    order_item = order_qs[0].orderItems.all()
    order_total = order_qs[0].get_totals

    return render(request,'app_payment/checkout.html',context={'form':form,'order_item':order_item,
    'order_total':order_total,
    'save_address':save_address
    
    })
