from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from .models import MyModel
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Vendor
import requests



def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("NuggetServer:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	else:
		form = NewUserForm()
	return render(request, template_name="NuggetServer/register.html", context={"register_form":form})


@login_required

def index(request):
    return render(request, 'NuggetServer/index.html')

def mac_database(request):
	if request.method == "POST":
		mac = request.POST.get("macaddr")
		ip = request.POST.get("ipaddr")
		# mac = "00-11-22-33-44-55"
		print(mac)
		url = "https://api.macvendors.com/" + mac
		payload = ""
		headers = {
		}
		response = requests.request("GET", url, headers=headers, data=payload)
		print(response.text)
		vendor = response.text
		Vendor.objects.create(
			mac_addr = mac,
			ip_addr = ip,
			vendor_name = vendor
		)
		context = {
			'vendors': Vendor.objects.all()
		}
		return render(request, "NuggetServer/database.html", context)
	else:
		return render(request, "NuggetServer/database.html")







def flash(request):
    return render(request, 'NuggetServer/flash.html')

def data(request):
    return render(request, 'NuggetServer/database.html')


