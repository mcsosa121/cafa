from django.http import HttpResponse
from django.template import Context, loader
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.utils.encoding import force_text
from cafaapp.models import House

class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, House):
            return force_text(obj)
        return super(LazyEncoder, self).default(obj)

from . import views


# Our RESTful api

@csrf_exempt
def create_contract(request):
    print("WOW")
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
        wow['lat']= houses[i].lat
        wow['lon']= houses[i].lon
        wow['lat']= houses[i].lat
        wow['street']= houses[i].street
        wow['city']= houses[i].city
        wow['zip']= houses[i].zip
        wow['img']= force_text(houses[i].img_docfile)


        cereal.append(wow)
    le = LazyEncoder(DjangoJSONEncoder)
    return json.dumps(cereal,  cls=LazyEncoder)



@csrf_exempt
def get_all_contracts(request):
    return HttpResponse(house_cereal(House.objects.all()), content_type='application/json')