from django.http import HttpResponse
from django.template import Context, loader
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.utils.encoding import force_text
from django.utils import timezone

from cafaapp.models import House
from cafaapp.models import Job

class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, House):
            return force_text(obj)
        return super(LazyEncoder, self).default(obj)

from . import views


# Our RESTful api

@csrf_exempt
def create_contract(request):
    if (request.method == 'POST'):
        docfile = request.FILES['img']
        lat = request.POST.get('lat', False)
        lon = request.POST.get('lon', False)
        street = request.POST.get('street', False)
        city = request.POST.get('city', False)
        state = request.POST.get('state', False)
        zip = request.POST.get('zip', False)
        contract = House(lat=lat, lon=lon,street=street,city=city,state=state,zip=zip,img_docfile=docfile)
        contract.save()
        return HttpResponseRedirect('views.dash')
    raise Http404("u missin stuff!!!!")

def house_cereal(houses):
    cereal = []
    for i in xrange(len(houses)):
        wow = {}
        wow['hid']= houses[i].hid
        wow['lat']= houses[i].lat
        wow['lon']= houses[i].lon
        wow['lat']= houses[i].lat
        wow['street']= houses[i].street
        wow['city']= houses[i].city
        wow['zip']= houses[i].zip
        wow['img']= '/cafa/media/' + force_text(houses[i].img_docfile)

        cereal.append(wow)
    le = LazyEncoder(DjangoJSONEncoder)
    return json.dumps(cereal,  cls=LazyEncoder)

@csrf_exempt
def make_job(request):
    if (request.method == 'POST'):
        type = request.POST.get('type', False)
        comment = request.POST.get('comment', False)
        scheduled_time = request.POST.get('scheduled_time', False)
        house_ref = House.objects.filter(hid=request.POST.get('house_ref', False))[0]

        j = Job(type=type,request_comment=comment,scheduled_time=scheduled_time,house_ref=house_ref)
        j.save()
        return HttpResponseRedirect('views.dash')
    raise Http404("u missin stuff!!!!")

@csrf_exempt
def complete_job(request):
    if (request.method == 'POST'):
        j = Job.objects.filter(jid=request.session['jid'])[0]
        j.completion_comment = request.POST.get('comment', False)
        j.completion_time = timezone.now()
        j.save() #TODO: Images here
        return HttpResponseRedirect('/cafa/ext/jobupdated')
    raise Http404("u missin stuff!!!!")

@csrf_exempt
def approve_job(request):
    if (request.method == 'POST'):
        j = Job.objects.filter(jid = request.POST.get('jid', False))[0]
        j.approval_status = True
        j.save() #TODO: Images here
        return HttpResponseRedirect('views.index')
    raise Http404("u missin stuff!!!!")

@csrf_exempt
def get_all_contracts(request):
    return HttpResponse(house_cereal(House.objects.all()), content_type='application/json')