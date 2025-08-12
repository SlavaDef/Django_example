from django.urls import path
from . import views


urlpatterns = [

    path('', views.news_home, name='news_home'), # оброблюємо /news/, views.news_home - виклик функції
    path('create/', views.create, name='create'),

]