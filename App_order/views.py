from django.shortcuts import render, get_object_or_404, redirect
from App_store.models import Product
from .models import Cart,Order
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def addToCart(request,pk):
    item = get_object_or_404(Product, pk=pk)
    order_item = Cart.objects.get_or_create(item=item,user=request.user, purchased=False)
    order_qs = Order.objects.filter(user=request.user, orderd = False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderItems.filter(item=item).exists():#ekta item order kora ase tokhon ekoi item add to cart korle ai function kaj korbe
            order_item[0].quantity += 1
            order_item[0].save()
            messages.success(request,'Update Product To Cart Successfully')
            return redirect('store')
        else:
            order.orderItems.add(order_item[0]) # ekta item order kora ase tokhon onno item add to cart korle ai function kaj korbe
            messages.info(request,'This Product was Added To Cart')
            return redirect('store')
    else:
        order = Order(user=request.user)#kono order item na kora thakle tokhon ekta item add to cart korle ai function kaj korbe
        order.save()
        order.orderItems.add(order_item[0])
        messages.success(request,'Add Product To Cart Successfully')
        return redirect('store')