from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

def index(request):
    return render(request, 'draw/index.html', {})

def channel(request):
    return render(request, 'draw/channel.html', {})

def gallery(request):
	return render(request, 'draw/gallery.html', {})

def connect(request):
	return render(request, 'draw/connect.html', {})

def support(request):
	return render(request, 'draw/support.html', {})

def portrait(request):
  return render(request, 'draw/portrait.html', {})

def solo(request):
  return render(request, 'draw/solo.html', {})

def sent(request):
  return render(request, 'draw/sent.html', {})

def room(request, room_name):
    return render(request, 'draw/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })
  
def smallDisplay(request):
   return render(request, "draw/smallDisplay.html")

def largeDisplay(request):
   return render(request, "draw/largeDisplay.html")
  