from django.urls import path
from . import views


urlpatterns = [

    path('', views.index), # якщо головна сторінка то виклик конкрет функції якоїсь
]