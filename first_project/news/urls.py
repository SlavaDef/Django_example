from django.urls import path
from . import views


urlpatterns = [

    path('', views.news_home, name='news_home'), # якщо головна сторінка то виклик конкрет функції якоїсь

]