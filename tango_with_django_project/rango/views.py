from django.http import HttpResponse
from django.shortcuts import render

def index (request):
	context_dict = {'boldmessage': "My name is Zhao Yunfeng!"}
	return render(request, 'rango/index.html', context=context_dict)

def about(request):
	return HttpResponse("Hello! <a href='/rango/'Index</a>")