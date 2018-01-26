from django.db import models
from resume.basemodel import AbstractDateModel
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse


class Client(AbstractDateModel):
    title = models.CharField(max_length=255)
    contacts = RichTextUploadingField(blank=True, null=True)
    desc = RichTextUploadingField(blank=True, null=True)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return self.title


class Project(AbstractDateModel):
    title = models.CharField(max_length=255)
    client = models.ForeignKey(Client, on_delete=None)
    desc = RichTextUploadingField(blank=True, null=True)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return '{} > {}'.format(self.title, self.client)

    def get_absolute_url(self):
        return reverse('project', args=[str(self.id)])

    def get_total_time(self):
        time = 0
        for milestone in self.milestone_set.all():
            for module in milestone.module_set.all():
                for task in module.task_set.all():
                    time += task.time
        return time

    def get_total_amount(self):
        amount = 0
        for milestone in self.milestone_set.all():
            for module in milestone.module_set.all():
                for task in module.task_set.all():
                    amount += task.get_total_for_task()
        return amount


class Milestone(AbstractDateModel):
    project = models.ForeignKey(Project, on_delete=None)
    title = models.PositiveSmallIntegerField()
    date_start = models.DateField(blank=True, null=True)
    date_finish = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = 'Milestone'
        verbose_name_plural = 'Milestones'

    def __str__(self):
        return '{} > Milestone #{} ({} - {})'.format(self.project, self.title, self.date_start, self.date_finish)


class Module(AbstractDateModel):
    milestone = models.ForeignKey(Milestone, on_delete=None)
    title = models.CharField(max_length=255)
    desc = RichTextUploadingField(blank=True, null=True)
    rate_per_hour = models.PositiveSmallIntegerField(default=25)

    class Meta:
        verbose_name = 'Module'
        verbose_name_plural = 'Modules'

    def __str__(self):
        return '{} > {}'.format(self.title, self.milestone.project)

    def get_total_time(self):
        time = 0
        for task in self.task_set.all():
            time += task.time
        return time

    def get_total_amount(self):
        amount = 0
        for task in self.task_set.all():
            amount += task.get_total_for_task()
        return amount


class Task(AbstractDateModel):
    module = models.ForeignKey(Module, on_delete=None)
    title = models.CharField(max_length=255)
    desc = RichTextUploadingField(blank=True, null=True)
    time = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return '{} > {}'.format(self.title, self.module)

    def get_total_for_task(self):
        return self.module.rate_per_hour * self.time
