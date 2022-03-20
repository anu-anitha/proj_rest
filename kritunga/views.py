from django.shortcuts import render
from .models import *
# Create your views here.


def chef_view(request):
	dynamicdata = Chef.objects.all()
	context = {'dynamic':dynamicdata}
	return render(request, 'chef.html', context)