from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponseRedirect
from twilio.rest import TwilioRestClient

def test_index(request):
	ACCOUNT_SID = "" 
	AUTH_TOKEN = "" 
	client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
	client.messages.create(
		to="+14235673625", 
		from_="+14234029660", 
		body="From our website!!!",  
	)
	return render(request, 'pushups/test_index.html')
def test_submit(request):
	return HttpResponseRedirect(reverse('pushups:test_index'))

