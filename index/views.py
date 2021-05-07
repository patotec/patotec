from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from .models import *
from .forms import *
from django.contrib import messages


def myindex(request):
	if request.method == 'POST':
		form = Contactform(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Thanks for your message we will repyl you shortly')
			return redirect('indexurl:index')
	else:
		form = Contactform()
  
	return render(request, 'index/index.html')



