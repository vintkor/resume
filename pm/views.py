from .models import Project, Task, Module, Client
from django.views.generic import ListView, DetailView, View
from django.shortcuts import render


class ProjectListView(ListView):
    template_name = 'pm/projects.html'
    context_object_name = 'projects'
    model = Project


class ProjectDetailView(DetailView):
    template_name = 'pm/project.html'
    context_object_name = 'project'

    def get_object(self, queryset=None):
        return Project.objects.prefetch_related(
            'milestone_set',
            'milestone_set__module_set',
            'milestone_set__module_set__task_set',
        ).get(pk=self.kwargs.get('pk'))


class TaskView(View):
    template_name = 'pm/ajax-container.html'

    def get(self, request, pk):
        task = Task.objects.get(pk=pk)
        context = {
            'desc': task.desc,
        }
        return render(request, self.template_name, context)


class ModuleView(View):
    template_name = 'pm/ajax-container.html'

    def get(self, request, pk):
        module = Module.objects.get(pk=pk)
        context = {
            'desc': module.desc,
        }
        return render(request, self.template_name, context)


class ProjectView(TaskView):
    template_name = 'pm/ajax-container.html'

    def get(self, request, pk):
        project = Project.objects.get(pk=pk)
        context = {
            'desc': project.desc,
        }
        return render(request, self.template_name, context)


class ClientView(TaskView):
    template_name = 'pm/ajax-container.html'

    def get(self, request, pk):
        client = Client.objects.get(pk=pk)
        context = {
            'desc': client.desc,
            'contacts': client.contacts
        }
        return render(request, self.template_name, context)
