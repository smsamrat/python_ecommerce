from turtle import title
from django.contrib import admin
from .models import Product,Category

# Register your models here.
class Categoryadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

class Productadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Product,Productadmin)
admin.site.register(Category,Categoryadmin)