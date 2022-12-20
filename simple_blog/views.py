from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views import generic
from django.urls import reverse
from .models import Post
# Create your views here.
def index(request):
    posts = Post.objects.filter(status = 1)
    context = {
        'posts' : posts
    }
    return render(request, 'postList.html', context)
def detail(request, slug):
    post = Post.objects.filter(slug = slug)
    if post.exists():
        post = post.first()
    else:
        return HttpResponse('<h1>Post Not Found</h1>')
    context = {
        'Post' : post
    }
    return render(request, 'postDetail.html', context)