
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_tasks, name='list_tasks'),
    path('complete_task/<int:pk>/', views.complete_task, name='complete_task'),
    path('add_task/', views.add_task, name='add_task'),
    path('change_task_status/<int:pk>/', views.change_task_status, name='change_task_status'),
]