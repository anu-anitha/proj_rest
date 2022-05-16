from django.contrib import admin
from kritunga.models import *
# Register your models here.

admin.site.register(Category)

admin.site.register(Customer)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'description',

                    'price', 'description', 'category_name']


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'description',
                    'product_price', 'product_image', 'category']
