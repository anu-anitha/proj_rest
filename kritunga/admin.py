from django.contrib import admin
from kritunga.models import *
# Register your models here.

admin.site.register(Category)

admin.site.register(Customer)


@admin.register(Chef)
class ChefAdmin(admin.ModelAdmin):
    list_display = [ 'chef_name','category_name' ,'chef_image',
                    'orders_completed', 'description', 'mobile','chef_availability']




@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'description',

                    'price', 'description', 'category_name','prepared_by']


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'description',
                    'product_price', 'product_image', 'category']
