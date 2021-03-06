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

    def get_total_money(self):
        return sum([i.amount for i in self.money_set.all()])


class Milestone(AbstractDateModel):
    project = models.ForeignKey(Project, on_delete=None)
    title = models.PositiveSmallIntegerField()
    date_start = models.DateField(blank=True, null=True)
    date_finish = models.DateField(blank=True, null=True)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        verbose_name = 'Milestone'
        verbose_name_plural = 'Milestones'
        ordering = ('my_order',)

    def __str__(self):
        return '{} > Milestone #{} ({} - {})'.format(self.project, self.title, self.date_start, self.date_finish)

    def is_done(self):
        modules = self.module_set
        if modules.all().count() == len([i for i in modules.all() if i.is_done()]):
            return True
        return False


class Module(AbstractDateModel):
    milestone = models.ForeignKey(Milestone, on_delete=None)
    title = models.CharField(max_length=255)
    desc = RichTextUploadingField(blank=True, null=True)
    rate_per_hour = models.PositiveSmallIntegerField(default=25)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        verbose_name = 'Module'
        verbose_name_plural = 'Modules'
        ordering = ('my_order',)

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

    def is_done(self):
        tasks = self.task_set
        if tasks.all().count() == tasks.filter(is_done=True).count():
            return True
        return False


class Task(AbstractDateModel):
    module = models.ForeignKey(Module, on_delete=None)
    title = models.CharField(max_length=255)
    desc = RichTextUploadingField(blank=True, null=True)
    time = models.PositiveSmallIntegerField(default=0)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)
    is_done = models.BooleanField(default=False, verbose_name='Выполнено')

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        ordering = ('my_order',)

    def __str__(self):
        return '{} > {}'.format(self.title, self.module)

    def get_total_for_task(self):
        return self.module.rate_per_hour * self.time


class Money(AbstractDateModel):
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Money'
        verbose_name_plural = 'Money'

    def __str__(self):
        return '{} - {}'.format(self.amount, self.project)
