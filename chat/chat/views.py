from django.shortcuts import render
from django.template import RequestContext

def lobby(request):
    return render(request, 'lobby.html')