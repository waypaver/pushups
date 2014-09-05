from django.shortcuts import render
from django_twilio.decorators import twilio_view
from twilio.twiml import Response

# Create your views here.
def index(request):
  return render(request, 'main/index.html')

@twilio_view
def sms(request):
  message = request.POST.get('Body', '')
  r = Response()
  r.message(message)
  return r
