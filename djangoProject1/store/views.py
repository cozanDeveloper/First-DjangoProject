from django.shortcuts import render
from  django.http import HttpResponse
# Create your views here.
def home(request):
    return  HttpResponse('<h1>Store home</h1>')
def about(request):
    return  HttpResponse('<h1>Store about</h1>')