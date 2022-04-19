from django.db import models

# Create your models here.

allocation_choices = (
    ('incomplete', 'incomplete'),
    ('pending', 'pending'),
    ('complete', 'complete')
)

class Category(models.Model):
    category_name=models.CharField(max_length=100)
    description=models.TextField(null=True,blank=True)
    category_image=models.ImageField(upload_to='images/', null=True, blank=True)
    def __str__(self):
    	return self.category_name
class Products(models.Model):
    product_name=models.CharField(max_length=100)
    description=models.TextField(null=True,blank=True)
    product_image=models.ImageField(upload_to='images/', null=True, blank=True)
    product_price=models.DecimalField(max_digits=20,decimal_places=2)
    category=models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True,)
    def __str__(self):
    	return self.product_name

class Chef(models.Model):
    chef_name=models.CharField(max_length=100,unique=True)
    chef_image=models.ImageField(upload_to='images/', null=True, blank=True)
    category_name=models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True,)
    orders_completed=models.IntegerField(default=0)
    description=models.TextField(null=True,blank=True)
    mobile=models.CharField(max_length=100)
    chef_availability=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
    	return self.chef_name


class Customer(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField()
    mobile=models.CharField(max_length=100)
    def __str__(self):
    	return self.username

class OrderItem(models.Model):
    category_name=models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True,)
    product_name=models.ForeignKey(Products, on_delete=models.SET_NULL, null=True, blank=True,)
    quantity=models.IntegerField()
    price=models.DecimalField(max_digits=20,decimal_places=2)
    description=models.TextField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    allocation=models.BooleanField(default=False)
    table_no=models.IntegerField()
    prepared_by=models.ForeignKey(Chef, on_delete=models.SET_NULL, null=True, blank=True,)
    status=models.CharField(max_length=20, choices=allocation_choices, default='incomplete')
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True,)
    todayorders = models.DateTimeField(auto_now=True)
    class Meta:
        db_table= "kritunga_orderitem"
    def __str__(self):
    	return self.description