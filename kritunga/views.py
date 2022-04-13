from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.core.exceptions import MultipleObjectsReturned
# Create your views here.

def chef_create(request):
	form = ChefForm()
	if request.method == 'POST':
		form = ChefForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
		return redirect('chef_view')
	context = {'form':form}
	return render(request, 'chef_create.html', context)

def chef_view(request):
	dynamicdata = Chef.objects.all()
	context = {'dynamic':dynamicdata}
	return render(request, 'chef_view.html', context)

def chef_read(request, id):
	dynamicdata = Chef.objects.get(pk=id)
	context = {'dynamic':dynamicdata}
	return render(request, 'chef_read.html', context)

def chef_update(request, id):
	z = Chef.objects.get(pk=id)
	form = ChefForm(instance=z) #old data
	if request.method == 'POST':
		form = ChefForm(request.POST, instance=z)
		if form.is_valid():
			form.save()
			return redirect('chef_view')
	context = {'form':form}
	return render(request, 'chef_update.html', context)

def chef_delete(request, id):
	Chef.objects.get(pk=id).delete()
	messages.info(request,"data deleted")
	return render(request, 'chef_delete.html')





#order Views
def order_create(request):# When user clicks on create order this fuciton will trigger
	form = OrderItemForm()#first render empty form || return render(request, 'order_create.html', context) || this code will take the form variable from here and it will render the empty form
	if request.method == 'POST': #when user clicks the submit button after filling the order details this line will get execute, if this IF condition stisfies we will enter in to the loop.
		form = OrderItemForm(request.POST, request.FILES)#This line of code will get all the data and files that are added in the form by user.
		if form.is_valid():#if the data entered in the form by user is a valid data, then enter in to the loop.
			get_category = request.POST.get('category_name')#Now the request is containing all the data that is entered by the user, out of that data we need only category. this line of code will bring what is the category that user selected.
			geting_prepared = OrderItem.objects.filter(status = 'incomplete', category_name = get_category)#From the existing orders we have to filter the orders which are incomplete and the category that user selected. this is being done just to get the chef's who are still working on the pirticular category, so that we can assign this order to the chef who is still preparing that category order.
			#print('+++++++++++++',geting_prepared)
			if geting_prepared:# if you get the list of chefs who are working on the same category, then enter in to the loop.
				chef_dict = {} #define an empty dict, this dict will have the {chef:orders_completed}
				#breakpoint()
				for i in geting_prepared:#iterate over the list of chefs(Querysets).
					chef_name_q = i.prepared_by #get the chef names who are preparing the incomplete orders.
					#print('----------------------',chef_name_q)
					get_chef = Chef.objects.filter(chef_name = chef_name_q).values_list('orders_completed', flat=True)#out of chefs who are preparing the incomplete orders, get their completed_orders number.
					for i in get_chef:#get the filtered list of chefs orders that are completed
						chef_dict[chef_name_q] = i #create a dict || dict['sravan'] = 2, dict['ravan'] = 3, chef_dict[sushanth]:1
				#print('DICT',chef_dict)
				chef_final = min(chef_dict, key=chef_dict.get)#Get the chefs orders who had prepared the less orders in a day.#get the key where the value is minimum#https://www.codegrepper.com/code-examples/python/how+to+find+the+minimum+value+in+a+dictionary+python
				get_chef = Chef.objects.get(chef_name = chef_final)
				obj = form.save(commit=False)
				obj.prepared_by = get_chef
				obj.save()
			else:#if the chef's are idle and not preparing any orders in line. all the existing orders are completed, if new order is comming up then assign the order to any available chef.
				get_chef = Chef.objects.filter(chef_availability = 1).first()
				obj = form.save(commit=False)#instace: hold before you save.
				obj.prepared_by = get_chef#before you save the customer order in database, assign a chef who is idle.
				obj.save()#save to DB


		return redirect('order_view')
	context = {'form':form}
	return render(request, 'order_create.html', context)

def order_view(request):
	dynamicdata = OrderItem.objects.all()
	context = {'dynamic':dynamicdata}
	return render(request, 'order_view.html', context)

def order_read(request, id):
	dynamicdata = OrderItem.objects.get(pk=id)
	context = {'dynamic':dynamicdata}
	return render(request, 'order_read.html', context)

def order_update(request, id):
	z = OrderItem.objects.get(pk=id)
	form = OrderItemForm(instance=z) #old data
	if request.method == 'POST':
		form = OrderItemForm(request.POST, instance=z)
		if form.is_valid():
			form.save()
			return redirect('order_view')
	context = {'form':form}
	return render(request, 'order_update.html', context)

def order_completed(request, id):
	OrderItem.objects.filter(pk=id).update(status = 'complete')
	chef_who_compltd_order = OrderItem.objects.filter(pk=id).values_list('prepared_by', flat=True)
	# orders_chef = Chef.objects.get(chef_name = chef_who_compltd_order)
	# # orders_chef_obj = 
	# total_orders = orders_chef+1
	# Chef.objects.filter(chef_name = chef_who_compltd_order).update(orders_completed = total_orders )
	messages.info(request,"Order completed")
	return redirect('order_view')


def order_delete(request, id):
	OrderItem.objects.get(pk=id).delete()
	messages.info(request,"data deleted")
	return render(request, 'order_delete.html')

def chef_orders(request, id):
	chefdata = Chef.objects.get(id=id)
	dynamicdata = OrderItem.objects.filter(prepared_by=chefdata)
	context = {'dynamic':dynamicdata}
	return render(request, 'order_view.html', context)

