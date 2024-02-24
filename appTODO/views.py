from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .forms import TaskForm
from .models import Task


# Create your views here.

def start(request):
    return HttpResponse("МММММ ХУЕТА!")

def all_user(reqest):
    users = User.objects.all()
    context = {
        'users' : users,
    }
    return render(reqest, 'listusers.html', {'users':users})


def pers_user(reqest, user_id):
    user = get_object_or_404(User, pk=user_id)
    context = {
        'user': user,
    }
    return render(reqest, 'pers_user.html', context)


def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('/')
    else:
        form = TaskForm()

    context={
        'form' : form
    }
    return render(request, 'create_task.html', context)


def get_in_user():
    return None


def get_task_user(request):
    user_id = request.user.id
    task = Task.objects.filter(created_by=user_id)
    # print(user_id, request.user)
    context = {
        'task': task,
    }

    return render(request, 'get_task_user.html', context)
    return None