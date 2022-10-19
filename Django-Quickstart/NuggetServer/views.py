from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect, HttpResponse
from .models import MyModel
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


@login_required
def myregister(request):
    return HttpResponse("register")

    






# def myhomepage(request):
#     print("home")

# def myflash(request):
#     print("flash")

# def mydatabase(request):
#     print("database")


def myview(request):
    myinstances = MyModel.objects.all()
    context = {
        'myinstances': myinstances
    }
    return render(request, 'NuggetServer/mytemplate.html', context)

def mycreate(request):
    myfield = request.POST['myfield']
    mymodel = MyModel(myfield=myfield)
    mymodel.save()
    return HttpResponseRedirect(reverse('NuggetServer:myview'))