from django.shortcuts import render
from . import models
from twilio.rest import Client

import time
import datetime








# Create your views here.

def home(request):
    return render(request,'base.html')

def speech(request):

    return render(request,'base.html')

def new_search(request,model=None):
    search=request.POST.get('search')
    date=request.POST.get('date-time')
    models.search.objects.create(search=search)

     # stuff for countdown
    fulldate = date
    s = fulldate.split('-')

    y = int(s[0])
    m = int(s[1])
    d = int(s[2])
    h = int(s[3])
    min = int(s[4])



    present_time = time.time()
    time_sleep = datetime.datetime(y, m, d, h, min,00)
    time.sleep(time_sleep.timestamp() - present_time)

    # stuff for twilio
    account_sid = 'AC911bd0d30df0c380d60627a53eb8f52d'
    auth_token = '8ecf3181b353f60a526b63b5305358d4'
    client = Client(account_sid, auth_token)

    message = search
    msg = client.messages.create(from_="+12028318347", body=message, to="+917032172247")
    print(date)
    print(msg.body)

    return render(request,'main/index.html',{'search':search})