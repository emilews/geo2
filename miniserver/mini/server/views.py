from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def ShowData(request):
    if request.method == 'POST':
        print(request.POST.get('data'))
    if request.method == 'GET':
        print(request.GET.get('data'))
    return HttpResponse('<h1>Page was not found</h1>') 
