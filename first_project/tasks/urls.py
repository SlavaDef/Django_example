from . import views
from django.urls import path




urlpatterns = [
    path('', views.index2, name='task'),
    path('create_task', views.create, name='create_task'),
    path('<int:pk>/update', views.TaskUpdateView.as_view(), name='task-update'),
    path('<int:pk>/delete', views.TaskDeleteView.as_view(), name='task-delete'),

]