from django.urls import path
from . import views

urlpatterns = [
    path('add-to-cart/<pk>/', views.addToCart, name='add_to_cart'),
    path('cart-view/', views.cartView, name='cart_view'),
    path('item-remove/<pk>/', views.itemRemove, name='item_remove'),
    path('item-increase/<pk>/', views.itemIncrease, name='item_increase'),
    path('item-decrease/<pk>/', views.itemDecrease, name='item_decrease'),

]