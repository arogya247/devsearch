from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def projects(request):
    page = 'the projects'
    number = 12
    context = {'page':page, 'number':number}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    return render(request, 'projects/single-project.html')

