from django.urls import path
from . import views


urlpatterns = [

    path('', views.news_home, name='news_home'), # оброблюємо /news/, views.news_home - виклик функції
    path('create/', views.create, name='create'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='news-update'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='news-delete'),

]


# '<int:pk>' відслідковуємо по primary key ніби змінний юрл на кшталт /news/1...or 2 or 3....
# views.NewsDetailView.as_view() вказуємо що ми працюємо зконкретним нашим класом