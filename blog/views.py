from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.

def allblogs(request):
    myblogs = Blog.objects
    return render(request, 'blog/allblogs.html', {'myblogs': myblogs})

def detail(request, blog_id):
    detblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'detblog': detblog})
