from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import * 

# Create your views here.

def index(request):
    # root route redirect to /shows
    return redirect('/shows')

def shows(request):
    # return a template that displays all the shows in a table
    context = {
        'all_shows': Show.objects.all()
    }
    return render(request, 'shows.html', context)

def new_show(request):
    # return a template containing the form for adding a new TV show
    return render(request, 'new.html')

def create_show(request):
    # add the show to the database, then redirect to /shows/<id>
    print(request.POST)
    if request.method == 'POST':
        print(request.POST['date'])
        errors = Show.objects.validator(request.POST)
        print(errors)
        if errors:
            for key, values in errors.items():
                messages.error(request, values)
            return redirect('/shows/new')
        Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['date'], description=request.POST['desc'])
        return redirect('/shows') # /shows/<id> ?
    return redirect('/shows')

def view_shows(request, id):
    # return a template that displays the specific show's information
    context = {
        'show': Show.objects.get(id=id)
    }
    return render(request, "one_show.html", context)

def edit_show(request, id):
    # return a template that displays a form for editing the TV show with the id specified in the url
    context = {
        'show': Show.objects.get(id=id)
    }
    return render(request, "edit.html", context)

def update_show(request, id):
    # update the specific show in the database, then redirect to /shows/<id>
    print(request.POST)
    if request.method == 'POST':
        errors = Show.objects.validator(request.POST)
        print(errors)
        if errors:
            for key, values in errors.items():
                messages.error(request, values)
            return redirect(f'/shows/{id}/edit')
        edit_show = Show.objects.get(id=id)
        edit_show.title = request.POST['title'] 
        edit_show.network=request.POST['network'] 
        edit_show.release_date=request.POST['date'] 
        edit_show.description=request.POST['desc']
        edit_show.save()
        return redirect(f"/shows/{id}")
    return redirect("/shows")

def delete_show(request, id):
    # delete the show with the specified id from the database, then redirect to /shows
    Show.objects.get(id=id).delete()
    return redirect("/shows")