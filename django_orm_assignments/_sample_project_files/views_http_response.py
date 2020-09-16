from django.shortcuts import render, redirect, HttpResponse
from .models import * 

# Create your views here.

def shows(request):
    # root route redirect to /shows
    # return a template that displays all the shows in a table
    return HttpResponse("Place holder for all shows")

def new_show(request):
    # return a template containing the form for adding a new TV show
    return HttpResponse("Placeholder to add new show")

def create_show(request):
    # add the show to the database, then redirect to /shows/<id>
    return HttpResponse("Placeholder to create new show")

def view_shows(request, id):
    # return a template that displays the specific show's information
    return HttpResponse(f"Placeholder to view show #{id} details")

def edit_show(request, id):
    # return a template that displays a form for editing the TV show with the id specified in the url
    return HttpResponse(f"Placeholder to edit show #{id}")

def update_show(request, id):
    # update the specific show in the database, then redirect to /shows/<id>
    return HttpResponse(f"Placeholder to update show #{id}")

def delete_show(request, id):
    # delete the show with the specified id from the database, then redirect to /shows
    return HttpResponse(f"Placeholder to delete show #{id}")