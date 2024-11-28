from django.shortcuts import render

from .models import Page

# Create your views here.

def history(request):
    return render(request, 'history.html')

def home(request):
    return render(request, 'home.html')

def other(request, page_id):
    page = Page.objects.get(id = page_id)
    return render(request, 'other.html', {'page': page})

def visit(request):
    return render(request, 'visit.html')