from django.shortcuts import render, redirect
import random
from datetime import datetime

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['activity'] = []
    return render(request, 'main_page.html')

def process(request):
    if request.method == 'POST':
        print("* Request method is", request.method)
        randy = 0
        timestamp = datetime.now().strftime("%m/%d/%Y %I:%M%p")
        # Farm earns 10-20 golds
        if request.POST['gold'] == 'farm':
            randy = random.randint(10, 20)
            request.session['gold'] += randy
            print(f"Earned {randy} golds from the farm ({timestamp})")
            request.session['activity'].append(f"Earned {randy} golds from the farm ({timestamp})")
        # Cave earns 5-10 golds
        if request.POST['gold'] == 'cave':
            randy = random.randint(5, 10)
            request.session['gold'] += randy
            request.session['activity'].append(f"Earned {randy} golds from the cave ({timestamp})")
        # House earns 2-5 golds
        if request.POST['gold'] == 'house':
            randy = random.randint(2, 5)
            request.session['gold'] += randy
            request.session['activity'].append(f"Earned {randy} house from the farm ({timestamp})")
        # Casino earns 0-20 golds
        if request.POST['gold'] == 'casino':
            randy = random.randint(0, 20)
            request.session['gold'] += randy
            request.session['activity'].append(f"Earned {randy} casino from the farm ({timestamp})")
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')
