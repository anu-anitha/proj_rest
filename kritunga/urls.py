from django.contrib import admin
from django.urls import path, include
from kritunga import views

urlpatterns = [
    path('chef_view',views.chef_view,name='chef_view'),#chefs fuction url
    path('chef_read/<str:id>',views.chef_read,name='chef_read'),
    path('chef_update/<str:id>',views.chef_update,name='chef_update'),
    path('chef_delete/<str:id>',views.chef_delete,name='chef_delete'),
    path('chef_create/',views.chef_create,name='chef_create'),
    path('chef_orders/<str:id>',views.chef_orders,name='chef_orders'),
    path('chef_data',views.chef_data,name='chef_data'),
]

#order urls
urlpatterns += [
    path('order_view',views.order_view,name='order_view'),#chefs fuction url
    path('order_read/<str:id>',views.order_read,name='order_read'),
    path('order_update/<str:id>',views.order_update,name='order_update'),
    path('order_delete/<str:id>',views.order_delete,name='order_delete'),
    path('order_create/',views.order_create,name='order_create'),
    path('order_completed/<str:id>',views.order_completed,name='order_completed'),
    path('table/', views.table_orders, name='table'),
    
]