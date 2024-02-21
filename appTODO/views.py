from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


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