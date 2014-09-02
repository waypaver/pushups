from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponseRedirect, HttpResponse

def test_index(request):
	return render(request, 'test_index.html')
	#return HttpResponse("Woo!")