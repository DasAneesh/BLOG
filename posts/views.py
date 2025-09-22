from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from posts.models import Posts

def posts(request: HttpRequest) -> HttpResponse:
    posts = Posts.objects.all()
    return render(request, 'posts/posts.html', {'title': 'Posts', 'posts': posts} )


def login(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Login page')

def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'posts/about .html', {'title': 'About', 'content' : 'About Page'})
# Create your views here.
