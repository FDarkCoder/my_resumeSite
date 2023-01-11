from django.shortcuts import render, HttpResponse
from . import models

def projects(request):
    projects = models.Projects.objects.all().order_by('-date')
    args = {"Projects":projects}
    return render(request, 'projects.html', args)

def project_detail(request, slug):
    project = models.Projects.objects.get(slug=slug)
    args = {"detail":project}
    return render(request, "/projects_detail.html")
