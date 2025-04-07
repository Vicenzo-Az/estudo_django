from django.http import HttpResponse

# from django.shortcuts import render


def blog(request):
    print('blog')
    return HttpResponse('blog do app')

def exemplo(request):
    print('exemplo blog')
    return HttpResponse('Exemplo de blog')