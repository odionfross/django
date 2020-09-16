from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.

# Render the homepage with the default value or subsequent values
def rand_word(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    request.session['count'] += 1
    request.session['word'] = get_random_string(length=14)
    print(request.session['count'])
    print(request.session['word'])
    return render(request, 'index.html')

# Reset the counter, generate a random number, and redirect back to the home page
def reset(request):
    request.session.flush()
    return redirect('/')