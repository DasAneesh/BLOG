from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpRequest, HttpResponse
from posts.forms import PostForm
from posts.models import Posts

def posts(request: HttpRequest) -> HttpResponse:
    posts = Posts.objects.all()
    return render(request, 'posts/posts.html', {'title': 'Posts', 'posts': posts} )


def login(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Login page')

def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'posts/about.html', {'title': 'About', 'content' : 'About Page'})

def create(request: HttpRequest):
    if request.method == 'POST':

        form = PostForm(request.POST)
        if form.is_valid():
            Posts.objects.create(
                title = form.cleaned_data['title'],
                text = form.cleaned_data['text'],
            )
            return redirect('posts')
    else:
        form = PostForm()
    return render(request, 'posts/create.html', {'form': form })


def retrieve(request: HttpRequest, post_id: int):
    post = Posts.objects.get(pk = post_id)
    return render(request, 'posts/retrieve.html', {'post': post})


def delete(request: HttpRequest, post_id: int):
    post = Posts.object.get(pk = post_id)
    if request.method == 'POST':
        post.delete()
        return('posts')
    else:
        return render(request, 'posts/retrieve.html', {'post': post})


def update(request: HttpRequest, post_id):
    post = get_object_or_404(Posts, id = post_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post.title = form.cleaned_data['title'],
            post.text = form.cleaned_data['text'],
            post.save()
            return redirect('posts')
    else:
        form = PostForm(initial={
            'title' : post.title,
            'text' : post.text, 
        })
    return render(request, 'posts/update.html', {'form': form, 'post': post})
