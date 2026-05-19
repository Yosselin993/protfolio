from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *

# Create your views here.
def home(request):
    context = {}
    templete = loader.get_template("index.html");
    return HttpResponse(templete.render(context, request))