from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return render(request, 'main/Index.html')


def demand(request):
    return render(request, 'main/demand.html')