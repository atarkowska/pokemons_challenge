from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<str:name>/', views.PokemonView.as_view(), name='detail'),
    
]
