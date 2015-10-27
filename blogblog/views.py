from django.shortcuts import render, render_to_response
from .models import Message
from django import forms
from blogblog.forms import New_messageForm
#from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect

def blog(request):
   f = {}
   f['message'] = Message.objects.all()
   return render(request, 'blog/massages.html', f)
