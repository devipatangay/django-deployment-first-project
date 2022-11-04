from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
import datetime
def f22(request):
     time=datetime.datetime.now()
     return HttpResponse("<center><h1>hello user...!!<br /><br />server date & time::"+str(time)+"</h1><hr /></center>")
     