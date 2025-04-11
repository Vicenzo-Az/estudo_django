from django.urls import path
from . import views as views
# MCT (MVC)

app_name = 'home'

# http://dominio.com.br/
urlpatterns = [
    path('', views.home, name='home'),
]
