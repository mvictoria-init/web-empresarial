from django.contrib import admin

from .models import Service

# Register your models here.

# que salgan todos los elementos en una tabla
@admin.register(Service)
class PostAdmin(admin.ModelAdmin):
    # escoger que elementos se veran en la vista como una lista
    list_display = ('id', 'title', 'subtitle', 'created',)
    # poner links en el elemento
    list_display_links = ('id', 'title',)
    # filtrar
    list_filter = ('created', 'updated',)
    # buscar
    search_fields = ('title', 'subtitle',)
    # solo lectura
    readonly_fields = ('created', 'updated',)
 