from django.shortcuts import render, redirect
from .models import Posts
from .forms import PostForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def all_posts_view(request):
    posts = Posts.objects.all()

    context = {
        'posts': posts
    }

    return render(request, 'posts/all_posts.html', context)

def post_detail(request, pk):
    post = Posts.objects.get(pk=pk)

    context = {
        'post': post
    }

    return render(request, 'posts/post_detail.html', context)


def post_update(request, pk):
    user = request.user
    post = Posts.objects.get(pk=pk)
    form = PostForm(request.POST or None, instance=post)

    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('posts:all_posts')

    context = {
        'form': form,
        'post': post,
        'user': user
    }

    return render(request, 'posts/update_post.html', context)

def post_delete(request, pk):
    user = request.user
    post = Posts.objects.get(pk=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('posts:all-posts')

    context = {
        'post': post,
        'user': user
    }

    return render(request, 'posts/post_delete.html', context)

@login_required()
def post_create(request):
    form = PostForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('posts:all-posts')

    context = {
        'form': form
    }

    return render(request, 'posts/create_post.html', context)