from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def f11(request):
    return HttpResponse("<center><h1>hello user....have a nice day</h1><hr /></center>")
    
