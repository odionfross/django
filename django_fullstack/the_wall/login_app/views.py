from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, UserManager
import bcrypt

# Have the root route render a page where users can register or log in
def index(request):
    context = {
        'action': request.GET.get('action', '')
    }
    return render(request, 'index.html', context)

# Complete the registration method, including showing errors if the input is invalid
def register(request):
    if request.method == "POST":
        errors = User.objects.validator(request.POST)
        # checks the post request data for error and prints the errors
        if errors:
            for key, values in errors.items():
                messages.error(request, values)
            return redirect('/?action=register')
        print("Printing POST request:", request.POST)
        # if successful, create the user instance and route to /success
        pw_hash = bcrypt.hashpw(request.POST['pwd'].encode(), bcrypt.gensalt()).decode()
        print("Password Hash: ", pw_hash)
        new_user = User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            birthday=request.POST['dob'],
            email=request.POST['email'],
            password=pw_hash
        )
        # can ccomplish the same thing with less code
        # else:
        # new_user = User.objects.register(request.POST)
        request.session['user_id'] = new_user.id
        print("Creating new user", new_user)
        return redirect('/wall')
    return redirect('/')

def login(request):
    if request.method == 'POST':
        # validate user form input and print errors
        errors = User.objects.login_validator(request.POST)
        if errors:
            for key, values in errors.items():
                messages.error(request, values)
            return redirect('/?action=login')
        # filter the database to find email
        logged_user = User.objects.filter(email=request.POST['email'])
        # if the query set is > 0 means we found the user
        if len(logged_user) > 0:
            # store the user instance in the variable
            logged_user = logged_user[0]
            # compare password in form to password in database
            if bcrypt.checkpw(request.POST['pwd'].encode(), logged_user.password.encode()):
                request.session['user_id'] = logged_user.id
                return redirect('/wall')
            return redirect('/wall')

    return redirect('/')