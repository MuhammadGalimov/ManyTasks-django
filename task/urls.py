from django.urls import path
from .views import add_task, show_projects, show_tasks

urlpatterns = [
    path('add/', add_task),
    path('tasks/', show_tasks),
    path('projects/', show_projects),
]
