from django.http import HttpResponse

def index (request):
	return HttpResponse("What should we eat <br/><a href='/rango/about/'>About</a>")

def about(request):
	return HttpResponse("Shiyu Wei <br/><a href='/rango/'>Index</a>")
