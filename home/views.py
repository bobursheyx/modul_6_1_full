from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def get_info(request):
    return HttpResponse('<h1>Hello Python<h1><hr/>')


def get_name(request):
    return HttpResponse('<h1>Hello Shaxriyor<h1><hr/>')

def get_view(request):
    return HttpResponse('Hi developer')