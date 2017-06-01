# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render, get_object_or_404
from django.template.loader import get_template

from .models import Operater, Pwm, camera
from .forms import OperaterForm, PwmForm
from mbedI2C import *

FORMAT_ZA_SLIKE = ['png', 'jpg', 'jpeg']

def gosti(request):
    return render(request, 'pogon/gosti.html')

def dokumentacija(request):
    if not request.user.is_authenticated():
        return render(request, 'pogon/login.html')
    else:
        nalog = Operater.objects.filter(kreirao=request.user)
        pwm = Pwm.objects.all()
        context = {
            'nalog': nalog,
            'pwm': pwm
        }
        return render(request, 'pogon/dokumentacija.html', context)

def detail(request, kreirao_id):
    operater = get_object_or_404(Operater, pk=kreirao_id)
    pwm = get_object_or_404(Pwm)
    return render(request, 'labos/detail.html', {'operater': operater, 'pwm':pwm})

def parametri(request):
    if not request.user.is_authenticated():
        return render(request, 'pogon/login.html')
    else:
        form = PwmForm()
        if request.method == 'POST':
            form = PwmForm(request.POST)
            if form.is_valid():
                context = {
                    'form':form,
                }
                form.save()
                return render(request, 'pogon/parametri.html', context)
        else:
            context = {
                'form':form
            }
    return render(request, 'pogon/parametri.html', context)

def prijava(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                obj = Operater.objects.filter(kreirao=request.user)
                return render(request, 'pogon/uprav_ploca.html', {'ispitivanje': obj})
            else:
                return render(request, 'pogon/gosti.html', {'error_message': 'Tvoj račun je blokiran od strane administratora'})
        else:
            return render(request, 'pogon/login.html', {'error_message': 'Neispravni korisnički podaci'})
    return render(request, 'pogon/login.html')

def odjava(request):
    logout(request)
    form = OperaterForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'pogon/gosti.html', context)


def nalog(request):
    nalog = Operater.objects.filter(kreirao=request.user)
    return render(request, 'pogon/nalog.html', {'nalog': nalog})

def pwm(request):
    pwm = Pwm.objects.all()
    return render(request, 'pogon/pwm.html', {'pwm': pwm})





# Upravljačka ploča
def ploca(request):
    # used to keep track when buttons are pressed twice.
    # you keep in cruise mode
    if not request.user.is_authenticated():
        return render(request, 'pogon/login.html')
    else:
        t = get_template('pogon/uprav_ploca.html')

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

