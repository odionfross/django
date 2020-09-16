from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

def index(request):
    # renders the courses on the homepage
    context = {
        'all_courses': Course.objects.all()
    }
    return render(request, 'index.html', context)

def create(request):
    if request.method == 'POST':
        print(request.POST)
        # checks if there's any errors
        errors = Course.objects.validator(request.POST)
        print(errors)
        # if any errors exist
        if errors:
            for key, values in errors.items():
                messages.error(request, values)
            return redirect('/')
        # if valid enter into the database
        Course.objects.create(
            name=request.POST['name'],
            description=request.POST['desc']
        )
    return redirect('/')

def single_course(request, id):
    context = {
        'delete_course': Course.objects.get(id=id)
    }
    return render(request, 'delete.html', context)

def delete_course(request, id):
    Course.objects.get(id=id).delete()
    return redirect("/")