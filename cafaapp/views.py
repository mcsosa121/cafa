from django.http import HttpResponse
from django.template import Context, loader

def login(request):
    template = loader.get_template("cafaapp/templates/login.html")
    return HttpResponse(template.render())	

def index(request):
    template = loader.get_template("cafaapp/templates/index.jade")
    return HttpResponse(template.render())	
