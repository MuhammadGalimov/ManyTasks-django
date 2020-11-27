from django.urls import path
from .views import add_task, add_project, show_projects, show_tasks, main_page

urlpatterns = [
    path('', main_page),
    path('add_task/', add_task),
    path('add_project/', add_project),
    path('tasks/', show_tasks),
    path('projects/', show_projects),
]
