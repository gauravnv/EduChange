from django.http import Http404

from django.shortcuts import render
from .models import User


def index(request):
    allUsers = User.objects.all()
    return render(request, 'Hestia/index.html', {'allUsers': allUsers})

def conditions(request):
    return render(request, 'Hestia/condition.html')

def detail(request, User_id):
    try:
        User = User.objects.get(pk=User_id)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    return render(request, 'Hestia/detail.html', {'User': User})

