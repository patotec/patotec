
from django.contrib.auth import authenticate,get_user_model,login,logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import View
from django.contrib import messages
from .models import *
from .forms import *


User = get_user_model()






def loginView(request):
	title = 'Login'
	if request.method == "POST":
		username = request.POST.get("username")
		password = request.POST.get("Password")
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			newurl = request.GET.get('next')
			if newurl:
				return redirect(newurl)
			return redirect('accurl:profile')
		else:
			messages.error(request, 'Invalid Credentials')
	context = { 'title':title}
	return render(request, 'acc/login.html', context)

@login_required(login_url='accurl:login')
def mydash(request):
	if request.method == 'POST':
		p_form = ProfileUpdateForm(request.POST,request.FILES, instance=request.user)
		if p_form.is_valid():
			p_form.save()
			messages.success(request, 'Your Profile Picture Has been updated congratulations')
			return redirect('accurl:profile')
	else:
		p_form = ProfileUpdateForm(instance=request.user)
	context = {'p_form': p_form,}
	return render(request, 'acc/profile.html', context)



def  signupView(request):
	title = 'Signup'
	if request.method == "POST":
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		username = request.POST.get('username')
		email = request.POST.get('email')
		phone = request.POST.get("phone")
		country = request.POST.get('country')
		salary = request.POST.get('salary')
		occupation = request.POST.get('occupation')
		password1 = request.POST.get("Password1")
		password2 = request.POST.get("Password2")

		if User.objects.filter(username=username).exists():
			messages.error(request, 'Username already taken')
			return redirect('accurl:signup')
		elif password1 != password2:
			messages.error(request, 'Passwords do not match')
			return redirect('accurl:signup')
		else:
			user = User.objects.create_user(username=username, password=password1, first_name=first_name, last_name=last_name, email=email,phone=phone,country=country,salary=salary, occupation=occupation)
			return redirect('accurl:login')
	return render(request, 'acc/signup.html')




	

def mylogout(request):
    logout(request)
    return redirect('accurl:login')


# Create your views here.