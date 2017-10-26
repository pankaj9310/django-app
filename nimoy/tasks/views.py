from django.urls import reverse
from django.core.urlresolvers import reverse_lazy
from .models import Task
from .forms import TaskForm
from nimoy.projects.models import Project
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.edit import FormMixin
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

class CreateTask(LoginRequiredMixin, CreateView):
    template_name = 'pages/task.html'
    model = Task
    fields = ['name', 'description', 'task_type', 'status', 'priority', 'due']
    success_url = reverse_lazy('project_list')
    def form_valid(self, form):
        project_id = self.request.POST.get('project_id').split('/')[-1]
        project = Project.objects.get(pk=project_id)
        if project:
            form.instance.owner = self.request.user
            form.instance.assignee = self.request.user
            form.instance.project = project
        return super(CreateTask, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'pages/task.html'
    model = Task
    fields = ['name', 'description', 'task_type', 'status', 'priority']
    def get_success_url(self):
        return reverse('task_detail', kwargs={'pk': self.object.pk})
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
    def get_success_url(self):
        return reverse('task_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(TaskDetails, self).get_context_data(**kwargs)
        context['form'] = self.form_class(initial={'task': self.object.pk})
        return context
