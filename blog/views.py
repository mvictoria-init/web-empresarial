from django.shortcuts import render

from .models import Post, Category

# Create your views here.
def blog(request):
    
    post = Post.objects.all()
    
    return render(request, 'blog.html', {'posts':post})

# category