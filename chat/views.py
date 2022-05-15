from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, redirect


from faker import Faker
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import ChatGrant

from .models import Room
from studdybuddy.models import Profile
import random


fake = Faker()


def all_rooms(request):
    rooms = Room.objects.all()
    try:
        user1 = Profile.objects.get(email=request.user.email)
        if request.method == "POST":
            user2email = request.POST.get("email", "")
            user2 = Profile.objects.get(email=user2email)
            # check that there are no other users with same email before saving
            try:
                slugforname = Room.objects.get(slug = user1.email + user2.email)
            # if profile with this email has not been created before
            except Room.DoesNotExist:
                slugforname = Room.objects.create(name= user1.first_name + " and " + user2.first_name + "'s room" , slug = user1.email + user2.email, description = "", user1 = user1, user2 = user2)
            return redirect("rooms/" + slugforname.slug)
    except:
        return redirect("home/")
    return render(request, 'chat/index.html', {'rooms': rooms})


def room_detail(request, slug):
    room = Room.objects.get(slug=slug)
    #profile = Profile.objects.get(email = request.user.email)
    #profile = Profile.objects.create(first_name="name")
    return render(request, 'chat/room_detail.html', {'room': room})


def token(request):
    hidden_number = str(random.randint(10000000000000000000,99999999999999999999))
    identity = request.GET.get('identity', request.user.email + hidden_number)
    #email = request.GET.get('email', request.user.email)
    #identity = Profile.objects.get(first_name=request.user.first_name)
    device_id = request.GET.get('device', 'default')  # unique device ID

    account_sid = settings.TWILIO_ACCOUNT_SID
    api_key = settings.TWILIO_API_KEY
    api_secret = settings.TWILIO_API_SECRET
    chat_service_sid = settings.TWILIO_CHAT_SERVICE_SID

    token = AccessToken(account_sid, api_key, api_secret, identity=identity)

    # Create a unique endpoint ID for the device
    endpoint = "MiniSlackChat:{0}:{1}".format(identity, device_id)

    if chat_service_sid:
        chat_grant = ChatGrant(endpoint_id=endpoint,
                               service_sid=chat_service_sid)
        token.add_grant(chat_grant)

    #profile = Profile.objects.create(first_name="name")
    response = {
        'identity': identity,
        'token': token.to_jwt(),
        #'email': email,
        #'username': 
    }

    return JsonResponse(response)

