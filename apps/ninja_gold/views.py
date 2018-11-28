# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.utils import timezone
import random

def index(request):
    if 'gold' not in request.session:
            request.session['gold'] = 0
    return render(request, 'ninja_gold/index.html')

def process(request, place_id):
    if request.method == "POST":
        if place_id == '1':
            dGold = random.randrange(10, 21)
            place = 'farm'
        elif place_id == '2':
            dGold = random.randrange(5, 11)
            place = 'cave'
        elif place_id == '3':
            dGold = random.randrange(2, 6)
            place = 'house'
        elif place_id == '4':
            dGold = random.randrange(-50, 51)
            place = 'casino'
        
        now = timezone.now().strftime('%Y/%m/%d %-I:%M %p')

        if dGold >= 0:
            activity_str = "Earned {} gold(s) from the {}! ({})".format(dGold, place, now)
            color = 'green'
        else:
            activity_str = "Entered a casino and lost {} golds... Ouch.. ({})".format(abs(dGold), now)
            color = 'red'
        
        if 'activities' not in request.session:
            request.session['activities'] = []
        
        activity = {
            "activity_str": activity_str,
            "color": color
        }
        request.session['activities'].insert(0, activity)
        request.session['gold'] += dGold
        request.session.modified = True
        return redirect('/')

    else:
        return redirect('/')
