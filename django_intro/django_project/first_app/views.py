from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    context = {
    	"name": "Noelle",
    	"favorite_color": "turquoise",
    	"pets": ["Bruce", "Fitz", "Georgie"]
    }
    return render(request, "index.html", context)

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog with a method named 'new'")

def create(request):
    return redirect("/")

def show(request, page_id):
    return HttpResponse(f"placeholder to display blog number: {page_id} with a method named 'show'")

def edit(request, page_id):
    return HttpResponse(f"placeholder to edit blog {page_id} with a method named 'edit'")

def destroy(request, page_id):
    return redirect("/")