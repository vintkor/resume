from django.contrib import admin
from .models import Client, Project, Milestone, Module, Task


class ProjectInline(admin.StackedInline):
    exclude = ('',)
    extra = 0
    model = Project


class MilestoneInline(admin.StackedInline):
    exclude = ('',)
    extra = 0
    model = Milestone


class ModuleInline(admin.StackedInline):
    exclude = ('',)
    extra = 0
    model = Module


class TaskInline(admin.StackedInline):
    exclude = ('',)
    extra = 0
    model = Task


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    inlines = (ProjectInline,)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = (MilestoneInline,)


@admin.register(Milestone)
class MilestoneAdmin(admin.ModelAdmin):
    inlines = (ModuleInline,)


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    inlines = (TaskInline,)
    list_editable = ('rate_per_hour',)
    list_display = ('__str__', 'rate_per_hour')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'time')
    list_editable = ('time',)
