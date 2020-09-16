from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def index(request):
    # retrieve and ninjas in the dojo
    context = {
        'all_dojos': Dojo.objects.all()
    }
    return render(request, 'index.html', context)

def add_dojo(request):
    print(request.POST)
    # creating a new dojo
    if request.method == 'POST':
        Dojo.objects.create(name=request.POST['dojo_name'], city=request.POST['city'], state=request.POST['state'])
        return redirect('/')
    return redirect('/')

def add_ninja(request):
    print(request.POST)
    # creating a new ninja
    if request.method == 'POST':
        Ninja.objects.create(first_name=request.POST['f_name'], last_name=request.POST['l_name'], dojo=Dojo.objects.get(id=request.POST['dojo_id']))
        return redirect('/')
    return redirect('/')