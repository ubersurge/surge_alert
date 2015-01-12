from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from .models import Greeting

# Create your views here.
def index(request):
	santamonica = {'start_latitude':'34.019454','start_longitude':'-118.491191','end_latitude':'34.019479','end_longitude':'-118.401718'}
	manhattanbeach = {'start_latitude':'33.881728','start_longitude':'-118.404121','end_latitude':'34.019479','end_longitude':'-118.401718'}
	westhollywood = {'start_latitude':'34.085036','start_longitude':'-118.359318','end_latitude':'34.019479','end_longitude':'-118.401718'}
	koreatown = {'start_latitude':'34.069112','start_longitude':'-118.281384','end_latitude':'34.019479','end_longitude':'-118.401718'}
	midwilshire = {'start_latitude':'34.057166','start_longitude':'-118.323956','end_latitude':'34.019479','end_longitude':'-118.401718'}
	downtown = {'start_latitude':'34.042943','start_longitude':'-118.260098','end_latitude':'34.019479','end_longitude':'-118.401718'}
	glendale = {'start_latitude':'34.137907','start_longitude':'-118.250141','end_latitude':'34.019479','end_longitude':'-118.401718'}
	northhollywood = {'start_latitude':'34.161161','start_longitude':'-118.358803','end_latitude':'34.019479','end_longitude':'-118.401718'}

	cities = []
	cities.append(santamonica)
	cities.append(manhattanbeach)
	cities.append(westhollywood)
	cities.append(koreatown)
	cities.append(midwilshire)
	cities.append(downtown)
	cities.append(glendale)
	cities.append(northhollywood)
	info = ''
	names = ["Santa Monica","Manhattan Beach","West Hollywood","Koreatown","Midwilshire","Downtown","Glendale","North Hollywood"]

	for i in cities:
		payload = cities[cities.index(i)]
		headers = {'Authorization':'Token ENTERYOURUBERTOKENHERE'}
		r = requests.get('https://api.uber.com/v1/estimates/price', params = payload, headers=headers)
		data = json.loads(r.text)
		info = info + (names[cities.index(i)]) + '    '
		info = info + (data['prices'][0]['display_name']) + '    '
		info = info + str((data['prices'][0]['surge_multiplier'])) + '  <br/><br/>'	
	return HttpResponse(info)


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

