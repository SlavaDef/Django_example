from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name='home'), # якщо головна сторінка то виклик конкрет функції якоїсь
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
]