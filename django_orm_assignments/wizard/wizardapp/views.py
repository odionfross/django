from django.shortcuts import render, render

# Create your views here.
def index(request):
    return render(request, '/')