from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.http import JsonResponse
from .models import Task
from .forms import TaskForm
from nimoy.projects.models import Project
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.edit import FormMixin
from django.views.generic.list import ListView

from rolepermissions.mixins import HasPermissionsMixin
from rolepermissions.checkers import has_permission, has_role

class CreateTask(CreateView):
    template_name = 'pages/task.html'
    model = Task
    fields = ['name', 'description', 'task_type', 'status', 'priority', 'due']
    success_url = '/'
    
    def form_valid(self, form):
        project_id = self.request.POST.get('project_id').split('/')[-1]
        project = Project.objects.get(pk=project_id)
        if(project):
            form.instance.owner = self.request.user
            form.instance.assignee = self.request.user
            form.instance.project = project
        return super(CreateTask, self).form_valid(form)

class TaskUpdate(UpdateView):
    template_name = 'pages/task.html'
    model = Task
    fields = ['name', 'description', 'task_type', 'status', 'priority']
    success_url = '/'
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(TaskUpdate, self).form_valid(form)


class TaskList(ListView):
    template_name = 'pages/task_list.html'
    model = Task

class TaskDetails(FormMixin, DetailView):
    model = Task
    template_name = 'pages/task_detail.html'
    form_class = TaskForm
    # def _get_tasks(self):
    #     tasks = self.object.all()
    #     return [{'name': x.name, 'description': x.description, 'assignee': x.assignee,
    #              'task_type': x.task_type, 'status': x.task_type, 'owner': x.owner} for x in testcases]

    def get_success_url(self):
        return reverse('task_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(TaskDetails, self).get_context_data(**kwargs)
        context['form'] = self.form_class(initial={'task': self.object.pk})
        # context['tasks'] = self._get_tasks()
        return context