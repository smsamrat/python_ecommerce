from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('cetegory/<str:slug>/',views.product_fetch_by_category, name='category'),
    path('product-details/<str:cat_slug>/<str:prod_slug>/', views.product_details, name='product_details'),
]