from django.contrib import admin

from .models import Category, Post

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated',)
    list_display = ('name', 'created', 'updated',)

admin.site.register(Category, CategoryAdmin)

# que salgan todos los elementos en una tabla
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # escoger que elementos se veran en la vista como una lista
    list_display = ('id', 'title', 'autor', 'post_categories', 'created',)
    # poner links en el elemento
    list_display_links = ('id', 'title',)
    # filtrar
    list_filter = ('autor__username', 'categories__name',)
    # buscar
    search_fields = ('title', 'autor__username',)
    # solo lectura
    readonly_fields = ('created', 'update',)
    # ordenar
    ordering = ('title', 'autor',)
    # ver fechas, es decir, por tiempo
    date_hierarchy = 'published'
    
    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    
    post_categories.short_description = 'Categorías'