from django.contrib import admin
from .models import Client, Project, Milestone, Module, Task, Money
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin


class MoneyInline(admin.TabularInline):
    extra = 0
    model = Money


class ProjectInline(admin.StackedInline):
    exclude = ('',)
    extra = 0
    model = Project


class MilestoneInline(SortableInlineAdminMixin, admin.StackedInline):
    exclude = ('',)
    extra = 0
    model = Milestone


class ModuleInline(SortableInlineAdminMixin, admin.StackedInline):
    exclude = ('',)
    extra = 0
    model = Module


class TaskInline(SortableInlineAdminMixin, admin.TabularInline):
    exclude = ('',)
    extra = 0
    model = Task


@admin.register(Money)
class MoneyAdmin(admin.ModelAdmin):
    list_display = ('project', 'amount', 'created')
    list_filter = ('project',)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    inlines = (ProjectInline,)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = (MilestoneInline, MoneyInline, )


@admin.register(Milestone)
class MilestoneAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = (ModuleInline,)


@admin.register(Module)
class ModuleAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = (TaskInline,)
    list_editable = ('rate_per_hour', 'milestone',)
    list_display = ('__str__', 'rate_per_hour', 'milestone',)


@admin.register(Task)
class TaskAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'time')
    list_editable = ('time',)
