from django.contrib import admin
from kritunga.models import *
# Register your models here.

admin.site.register(Category)

admin.site.register(Customer)
<<<<<<< HEAD
@admin.register(Chef)
class ChefAdmin(admin.ModelAdmin):
    list_display = [ 'chef_name','category_name' ,'chef_image',
                    'orders_completed', 'description', 'mobile','chef_availability']

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = [ 'product_name', 'description',
=======

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'description',
>>>>>>> 99d8b8d5e17d3cfce992398ffb9d42cc4f779b4c
                    'price', 'description', 'category_name']


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'description',
                    'product_price', 'product_image', 'category']
