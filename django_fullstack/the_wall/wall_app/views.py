from django.shortcuts import render, redirect
from login_app.models import User, UserManager
import datetime
from .models import *

def wall(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'all_messages': Message.objects.all().order_by("-updated_at"), # latest message on top/first
        'all_comments': Comment.objects.all().order_by("updated_at"), # oldest comment on top/first
        'current_time_offset': datetime.datetime.now() - datetime.timedelta(minutes=30)
    }
    current_time = datetime.datetime.now()
    time_offset = datetime.timedelta(minutes=30)
    offset_time = current_time - time_offset
    print("****current_time", current_time)
    print("****offset_time", offset_time)
    print (current_time > offset_time)

    if request.method == 'POST':
        print("Entering message post method")
        Message.objects.create(user=User.objects.get(id=request.session['user_id']), message=request.POST['message'])
        return redirect('/wall')
    return render(request, 'the_wall.html', context)

def delete_message(request, mess_id):
    Message.objects.get(id=mess_id).delete()
    return redirect('/wall')

def comment(request, mess_id):
    if request.method == 'POST':
        print("Entering comment post method")
        Comment.objects.create(user=User.objects.get(id=request.session['user_id']), message=Message.objects.get(id=mess_id), comment=request.POST['comment'])
    return redirect('/wall')

def logout(request):
    request.session.clear()
    return redirect('/')


