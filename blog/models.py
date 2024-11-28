from django.db import models

from django.utils.timezone import now #para published, modificar fecha y hora de publicacion

from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'categoría'
        verbose_name_plural = 'categorías'
        ordering = ['-created']

    def __str__(self):
        return self.name


# Create your models here.

class Post(models.Model):
    image = models.ImageField(verbose_name='Imagen', upload_to='blog', null=True, blank=True)
    
    title = models.CharField(max_length=200, verbose_name='Título')
    content = models.TextField(verbose_name='Contenido')
    
    autor = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)
    
    categories = models.ManyToManyField(Category, verbose_name='Categoria')
    
    published = models.DateTimeField(default= now, verbose_name='Fecha de publicación')
    
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    update = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')
    
    class Meta:
        # cambiar el nombre en el menu principal
        verbose_name='Publicación'
        # cambiar el nombre en el menu principal
        verbose_name_plural='Publicaciones'
        # ordenar elementos del ultimo al primero
        ordering = ['created']
        
    def __str__(self):
        return self.title