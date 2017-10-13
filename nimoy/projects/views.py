from django.urls import reverse
from .models import Project
from .forms import ProjectForm
from nimoy.tasks.models import Task
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.edit import FormMixin
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

class CreateProject(LoginRequiredMixin, CreateView):
    template_name = 'pages/project.html'
    model = Project
    fields = ['name', 'description', 'project_type']
    success_url = '/'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(CreateProject, self).form_valid(form)

class ProjectUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'pages/project.html'
    model = Project
    fields = ['name', 'description', 'project_type']
    success_url = '/'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(ProjectUpdate, self).form_valid(form)


class ProjectList(ListView):
    template_name = 'pages/project_list.html'
    model = Project

class ProjectDetails(FormMixin, DetailView):
    model = Project
    template_name = 'pages/project_detail.html'
    form_class = ProjectForm

    def _get_tasks(self):
        tasks = Task.objects.filter(project=self.object.pk)
        return [{'name': x.name, 'description': x.description, 'assignee': x.assignee,
                 'task_type': x.task_type, 'status': x.status, 'owner': x.owner,
                 'priority': x.priority, 'pk': x.id} for x in tasks]

    def _get_graph_data(self):
        status_data = {'To Do':0, 'Progress':0, 'Completed':0}
        tasks = Task.objects.filter(project=self.object.pk)
        for task in tasks:
            status_data[task.status] += 1
        data_values = [status_data['To Do'], status_data['Progress'], status_data['Completed']]
        return data_values
    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(ProjectDetails, self).get_context_data(**kwargs)
        context['form'] = self.form_class(initial={'project': self.object.pk})
        context['tasks'] = self._get_tasks()
        context['data_values'] = self._get_graph_data()
        return context
