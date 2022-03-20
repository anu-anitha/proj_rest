from django.contrib import admin
from django.urls import path, include
from kritunga import views

urlpatterns = [
    path('chef',views.chef_view,name='chef_view'),#chefs fuction url
    #path('order',views.order_view,name='order'),#order fuction url
    path('chef_read',views.chef_read,name='chef_read'),
    path('chef_update',views.chef_update,name='chef_update'),
    path('chef_delete',views.chef_delete,name='chef_delete'),
]