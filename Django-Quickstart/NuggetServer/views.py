from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from .models import MyModel
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("NuggetServer:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="NuggetServer/register.html", context={"register_form":form})

    

def index(request):
    return render(request, 'NuggetServer/index.html')

def login(request):
    return render(request, 'accounts/login.html')


@login_required

def homepage(request):
    return render(request, 'NuggetServer/home.html')













def flash(request):
    return render(request, 'NuggetServer/flash.html')

def data(request):
    return render(request, 'NuggetServer/database.html')


def mycreate(request):
    myfield = request.POST['myfield']
    mymodel = MyModel(myfield=myfield)
    mymodel.save()
    return HttpResponseRedirect(reverse('NuggetServer:myview'))