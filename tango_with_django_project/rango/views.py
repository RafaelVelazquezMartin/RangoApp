from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
	html = "<html><body>Rango says hey there partner! <br/> <a href='/rango/about/'>About</a></body></html>"
	return HttpResponse(html)
	
def about(request):
	html = "<html><body>Rango says this is the about page.<br/> <a href='/rango/'>Index</a></body></html>"
	return HttpResponse(html)


#Deploy server command -- python manage.py runserver