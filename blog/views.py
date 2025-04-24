from django.shortcuts import render
from typing import Any
from blog.data import posts
from django.http import HttpRequest, Http404

def blog(request):
    print('blog')

    context = {
        # 'text': 'Olá Blog',
        'title': 'Blog',
        'posts': posts
    }

    return render(
        request, 
        'blog/index.html',
        context,
    )

def post(request: HttpRequest, post_id: int):
    found_post: dict[str, Any] | None = None

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break

    if found_post is None:
        raise Http404('Post não existe.')

    context = {
        # 'text': 'Olá Blog',
        'title': f'Post {found_post['id']}',
        'post': found_post
    }

    return render(
        request, 
        'blog/post.html',
        context,
    )

def exemplo(request):
    print('exemplo blog')

    context = {
        'text': 'Olá Exemplo do blog',
        'title': 'Exemplo do blog'    
    }

    return render(
        request, 
        'blog/exemplo.html',
        context,
    )