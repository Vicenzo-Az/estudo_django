from django.shortcuts import render


def blog(request):
    print('blog')

    context = {
        'text': 'Ola blog',
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
        'text': 'Ola exemplo do blog',
        'title': 'Exemplo do blog'    
    }

    return render(
        request, 
        'blog/exemplo.html',
        context,
    )