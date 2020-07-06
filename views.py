from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def cse (request):
    return HttpResponse("Welcome on CSE Page")

def etc(request):
    return HttpResponse("Welcome on ETC Page")

def mech(request):
    return HttpResponse("Welcome on MECH Page")

def civil(request):
    return HttpResponse("Welcome on CIVIL Page")