from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# get
def index(request):
    return HttpResponse('<strong>你好</strong>')
