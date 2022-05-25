from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login, authenticate
import json
import datetime
import base64

from .models import Profile, Gender, Photo

# Create your views here.

def index(request):
    return render('index.html')


def register(request):
    try:
        data = json.loads(request.body)
    except:
        return HttpResponse(status=400)

    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    gender = data.get('gender')
    genders_interested_in = data.get('genders_interested_in')
    location = data.get('location')
    locations_interested_in = data.get('locations_interested_in')
    relationship_types_interested_in = data.get('relationship_types_interested_in')
    birth_date = data.get('birth_date')
    photos = data.get('photos')

    if username is None:
        return HttpResponse(status=400)

    if Profile.objects.filter(username=username).count() > 0:
        return HttpResponse(status=409)
    
    if password is None:
        return HttpResponse(status=400)

    if email is None:
        return HttpResponse(status=400)

    if gender is None:
        return HttpResponse(status=400)

    if genders_interested_in is None:
        return HttpResponse(status=400)

    if location is None:
        return HttpResponse(status=400)

    if locations_interested_in is None:
        return HttpResponse(status=400)

    if relationship_types_interested_in is None:
        return HttpResponse(status=400)

    if birth_date is None:
        return HttpResponse(status=400)

    if photos is None:
        return HttpResponse(status=400)
    

    try:
        user = Profile.objects.create(username=username, email=email, gender=Gender.objects.get(id=gender), genders_interested_in=Gender.objects.filter(id=genders_interested_in), birth_date=datetime.datetime(birth_date.year, birth_date.month, birth_date.day), photos=photos)
        user.set_password(password)
        for index, photo in enumerate(photos):
            Photo.objects.create(profile=user, photo=base64.b64decode(photo), priority=index)
        login(user)
        return JsonResponse({"user": user.serialize()})
    except:
        return HttpResponse(status=409)
    
def login(request):
    try:
        data = json.loads(request.body)
    except:
        return HttpResponse(status=400)
    username = data.get('username')
    password = data.get('password')
    user = authenticate(username, password)
    if user is not None:
        login(user)
        return JsonResponse({"user": user.serialize()})


