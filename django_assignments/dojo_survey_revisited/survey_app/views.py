from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'form.html')

def process(request):
    print(request.POST, "a POST request is being made to this route")
    
    request.session['name'] = request.POST['full_name']
    request.session['loc'] = request.POST['location']
    request.session['lang'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    return redirect('/submit')

def submit(request):
    print('got here from redirect!')
    return render(request, 'result.html')