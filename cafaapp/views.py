from django.http import HttpResponse
from django.template import Context, loader
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

from cafaapp.models import Job


# Lazy user creation
#todo
user, created = User.objects.get_or_create(username='admin', email='admin@example.com')
if created:
    user.set_password('password')

@csrf_exempt
def loginext(request):
    if request.method == 'GET':
        template = loader.get_template("cafaapp/templates/login_ext.jade")
        return HttpResponse(template.render())
    elif request.method == 'POST':
        username = request.POST.get('username', False)
        password = request.POST.get('pwd', False)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            print("Success")
            template = loader.get_template("cafaapp/templates/index.jade")
            return HttpResponse(template.render())
        else:
            # Return an 'invalid login' error message.
            #login(request, user) #todo
            print("FAIL")
            template = loader.get_template("cafaapp/templates/login_ext.jade")
            return HttpResponse(template.render())

@csrf_exempt
def dash(request):
    template = loader.get_template("cafaapp/templates/int/dashboard.jade")
    return HttpResponse(template.render())

@csrf_exempt
def loginuser(request):
    if request.method == 'GET':
        template = loader.get_template("cafaapp/templates/login_int.jade")
        return HttpResponse(template.render())
    elif request.method == 'POST':
        username = request.POST.get('username', False)
        password = request.POST.get('pwd', False)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            print("Success")
            template = loader.get_template("cafaapp/templates/int/dashboard.jade")
            return HttpResponse(template.render())
        else:
            # Return an 'invalid login' error message.
            #login(request, user) #todo
            print("FAIL")
            template = loader.get_template("cafaapp/templates/login_int.jade")
            return HttpResponse(template.render())

@csrf_exempt
def index(request):
    template = loader.get_template("cafaapp/templates/index.jade")
    return HttpResponse(template.render())

@csrf_exempt
def jobupdated(request):
    template = loader.get_template("cafaapp/templates/ext/job_updated.jade")
    return HttpResponse(template.render())

@csrf_exempt
def newcontract(request):
    template = loader.get_template("cafaapp/templates/int/new_contract.jade")
    return HttpResponse(template.render())

@csrf_exempt
def mfga(request):
    template = loader.get_template("cafapp/templates/int/mfga.jade")
    return HttpResponse(template.render())

@csrf_exempt
def viewcontract(request):
    template = loader.get_template("cafaapp/templates/int/view_contract.jade")
    return HttpResponse(template.render())

@csrf_exempt
def job(request):
    if request.method == 'POST':
        j = request.POST.get('jid',False)
        print(j)
        actualJob = Job.objects.filter(jid = j)[0]
        request.session['jid']=j
        template = loader.get_template("cafaapp/templates/ext/do_job.jade")
        return HttpResponse(template.render())
