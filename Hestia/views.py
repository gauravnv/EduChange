from django.http import Http404

from django.shortcuts import render
from .models import Parent


def index(request):
    allParents = Parent.objects.all()
    return render(request, 'Hestia/index.html', {'allParents': allParents,})

def detail(request, Parent_id):
    try:
        Parent = Parent.objects.get(pk=Parent_id)
    except Parent.DoesNotExist:
        raise Http404("Parent does not exist")
    return render(request, 'Hestia/detail.html', {'Parent': Parent})