# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404
from django.template.loader import get_template

from .models import Operater
from .forms import UserForm
#from wiPiBotClient import *

FORMAT_ZA_SLIKE = ['png', 'jpg', 'jpeg']

def gosti(request):
    return render(request, 'pogon/gosti.html')

def ploca(request):
    if not request.user.is_authenticated():
        return render(request, 'pogon/gosti.html')
    else:
        return render(request, 'pogon/uprav_ploca.html')

def dokumentacija(request):
    if not request.user.is_authenticated():
        return render(request, 'pogon/gosti.html')
    else:
        return render(request, 'pogon/dokumentacija.html')

def formular(request, operater_id):
    if not request.user.is_authenticated():
        return render(request, 'pogon/gosti.html')
    else:
        return render(request, 'pogon/parametri.html')

def detaljno(request):
    if not request.user.is_authenticated():
        return render(request, 'pogon/gosti.html')
    else:
        return render(request, 'pogon/detaljno.html')

def prijava(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                operater = Operater.objects.filter(kreirao=request.user)
                return render(request, 'pogon/uprav_ploca.html', {'operater': operater})
            else:
                return render(request, 'pogon/login.html', {'error_message': 'Tvoj račun je blokiran od strane administratora'})
        else:
            return render(request, 'pogon/login.html', {'error_message': 'Neispravni korisnički podaci'})
    return render(request, 'pogon/login.html')

def odjava(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'pogon/gosti.html', context)

'''
# Upravljačka ploča
def dashboard(request):
    # used to keep track when buttons are pressed twice.
    # you keep in cruise mode

    t = get_template('dashboard.html')

    if 'cmd' in request.GET and request.GET['cmd']:
        cmd = request.GET['cmd']

        if cmd == 'led':
            blink()

        # Dodao "pause" da bude enA i enB = 0
        if (cmd == 'pause'):
            speed_control(cmd)

        if (cmd == 'up') or (cmd == 'down'):
            speed_control(cmd)

        if cmd == 'record':
            camera.record()

        if cmd == 'stop-record':
            camera.stop()

        if cmd == 'take-photo':
            camera.photo()

        if cmd == 'motor-stol':
            motor_select(cmd)

        if cmd == 'motor-goredolje':
            motor_select(cmd)

        if cmd == 'motor-obrada':
            motor_select(cmd)

        motor_control(cmd)

    return HttpResponse(t.render())
'''
