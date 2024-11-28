from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Service

# Create your views here.

def service(request):
    services = Service.objects.all().order_by('-created')  # Obtén todos los posts ordenados por fecha
    
     # Paginación con 10 productos por página
    paginator = Paginator(services, 3)
    page_number = request.GET.get('page')
    try:
        page = paginator.page(page_number)
    except PageNotAnInteger:
        # Si la página no es un entero, muestra la primera página
        page = paginator.page(1)
    except EmptyPage:
        # Si la página está fuera de rango, muestra la última página
        page = paginator.page(paginator.num_pages)
    
    return render(request, 'service.html', {'page':page})