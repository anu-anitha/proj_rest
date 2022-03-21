from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
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
def order_create(request):
	form = OrderItemForm()
	if request.method == 'POST':
		form = OrderItemForm(request.POST, request.FILES)
		if form.is_valid():
			get_category = request.POST.get('category_name')
			geting_prepared = OrderItem.objects.filter(status = 'incomplete', category_name = get_category)
			for i in geting_prepared:
				print(i.prepared_by)
			form.save()
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

def order_delete(request, id):
	OrderItem.objects.get(pk=id).delete()
	messages.info(request,"data deleted")
	return render(request, 'order_delete.html')













# def order(request):
# 	avail_chef = Chef.objects.filter(status=True)
# 	orderform = OrderItemForm()
# 	if request.method == 'POST':
# 		form = OrderItemForm(request.POST)
# 		chefname = request.POST.get('chef_name')
# 		if form.is_valid():
# 			get_category = request.POST.get('category_name')#biryani
# 			print(get_category)
# 			geting_prepared = OrderItem.objects.filter(status = 'incomplete', category_name = get_category) #Get all orders which are getting prepared in kitchen.#5
# 			print(geting_prepared)
# 			form.save()
# 		return redirect('chef_view')


# # order()