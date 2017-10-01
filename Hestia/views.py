from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>This is Hestia's Homepage</h1>")

def detail(request, Parent_id):
    return HttpResponse("<h2>Details for Parent id: " + str(Parent_id) + "</h2>")