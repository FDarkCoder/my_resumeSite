from django.shortcuts import render
from django.shortcuts import HttpResponse


def AboutMe(request):
    return render(request, 'index.html')
