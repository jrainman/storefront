from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#  takes a request handler
#  takes request and returns response

def calculate():
    x = 1
    y = 2
    return x

def say_hello(request):
    #  pull data from database
    #  transform data
    #  send emails
    # return HttpResponse('Hello World')
    x = calculate()

    return render(request, 'hello.html', {'name': 'Josh'})