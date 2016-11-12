from django.http import HttpResponse
from django.template import Context, loader

def login(request):
    template = loader.get_template("cafaapp/views/login.html")
    return HttpResponse(template.render())	

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
