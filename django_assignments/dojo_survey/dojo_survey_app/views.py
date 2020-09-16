from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def summary(request):
    context = {
        'name': request.POST['full_name'],
        'loc': request.POST['location'],
        'lang': request.POST['fav_lang'],
        'comment': request.POST['comment']
    }
    if request.method == "GET":
        print("a GET request is being made to this route")
        return render(request, "/")
    if request.method == "POST":
        print(request.POST, "a POST request is being made to this route")
        return render(request, 'summary.html', context)
    