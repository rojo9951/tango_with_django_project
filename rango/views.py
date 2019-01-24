from django.shortcuts import render

#importing HttpResponse
from django.http import HttpResponse

#create a view (called index)
def index(request):
    #returns string representing content of page to send to client
    return HttpResponse("Rango says hey there partner!")
