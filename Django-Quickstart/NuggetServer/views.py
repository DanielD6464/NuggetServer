from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from .models import MyModel
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import requests


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		print("form", form)
		form.cleaned_data['username']
		form.cleaned_data['email']
		form.cleaned_data['password1']
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("NuggetServer/index.html")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="NuggetServer/register.html", context={"register_form":form})



@login_required

def index(request):
    return render(request, 'NuggetServer/index.html')

# def homepage(request):
#     return render(request, 'NuggetServer/home.html')

def database(request):
	response=request.get('https://api.macvendors.com/FC-A1-3E-2A-1C-33').json()
	return render(request, database, {'response', response})












def flash(request):
    return render(request, 'NuggetServer/flash.html')

def data(request):
    return render(request, 'NuggetServer/database.html')


def mycreate(request):
    myfield = request.POST['myfield']
    mymodel = MyModel(myfield=myfield)
    mymodel.save()
    return HttpResponseRedirect(reverse('NuggetServer:myview'))