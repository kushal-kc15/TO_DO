from django.urls import path, include
from . import views

urlpatterns = [
    path('addTask/', views.addTask, name='add_task'),
    path('<int:task_id>/delete/', views.deleteTask, name='delete_task'),
    path('<int:pk>/complete/', views.completeTask, name='complete_task'),
    path('<int:pk>/', views.undoneTask, name='undone_task'),
    path('<int:pk>/update/', views.updateTask, name='update_task'),
]