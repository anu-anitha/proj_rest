from django.contrib import admin
from kritunga.models import *
# Register your models here.

admin.site.register(Category)

admin.site.register(Customer)
<<<<<<< HEAD

=======

@admin.register(Chef)
class ChefAdmin(admin.ModelAdmin):
    list_display = [ 'chef_name','category_name' ,'chef_image',
                    'orders_completed', 'description', 'mobile','chef_availability']


>>>>>>> a93f7ba060c8b78a56b2793dab0ef7078b3348a1

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'description',

                    'price', 'description', 'category_name']


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'description',
                    'product_price', 'product_image', 'category']
