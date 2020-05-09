from django.shortcuts import render
from django.http import HttpResponse

from .tasks import hello_world

def index(request):
# Create your views here.
	hello_world.delay()
	return HttpResponse("Hello, world.")
	