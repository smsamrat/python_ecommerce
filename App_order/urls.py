from django.urls import path
from . import views

urlpatterns = [
    path('add-to-cart/<pk>/', views.addToCart, name='add_to_cart'),
]