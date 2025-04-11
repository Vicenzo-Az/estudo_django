from django.shortcuts import render


def home(request):
    print('home')

    context = {
        'text': 'Olá Home',
        'title': 'Home'    
    }

    return render(
        request, 
        'home/index.html',
        context,        
    )

