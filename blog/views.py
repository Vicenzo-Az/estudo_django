from django.shortcuts import render


def blog(request):
    print('blog')

    context = {
        'text': 'Olá Blog',
        'title': 'Blog'    
    }

    return render(
        request, 
        'blog/index.html',
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