from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Task, Project
from .forms import TaskAddForm


def main_page(request):
    return render(request, 'index.html')


def add_task(request):
    if request.method == 'POST':
        task_add_form = TaskAddForm(request.POST)

        if task_add_form.is_valid():
            new_task = Task(name=task_add_form.cleaned_data['name'],
                            descr=task_add_form.cleaned_data['descr'],
                            added_date=task_add_form.cleaned_data['added_date'],
                            end_date=task_add_form.cleaned_data['end_date'],
                            done=False,
                            project_id=task_add_form.cleaned_data['project_id'])
            new_task.save()

            return HttpResponseRedirect('/tasks/')

    else:
        task_add_form = TaskAddForm()

    return render(request, 'add_task.html', {'task_add_form': task_add_form})


def add_project(request):
    pass


def show_tasks(request):
    tasks_list = Task.objects.order_by('name')
    context = {
        'tasks_list': tasks_list,
    }

    return render(request, 'tasks.html', context)


def show_projects(request):
    projects_list = Project.objects.order_by('added_date')
    context = {
        'projects_list': projects_list,
    }

    return render(request, 'projects.html', context)
