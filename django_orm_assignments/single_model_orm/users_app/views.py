from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def index(request):
    # retrieve and display all the users
    context = {
        'all_users': User.objects.all()
    }
    return render(request, 'users.html', context)

def new_user(request):
    print(request.POST)
    # creating a new user
    if request.method == 'POST':
        new_user = User.objects.create(first_name=request.POST['f_name'], last_name=request.POST['l_name'], email_address=request.POST['email_address'], age=request.POST['age'])
        return redirect('/')
    return redirect('/')