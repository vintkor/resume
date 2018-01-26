# Generated by Django 2.0.1 on 2018-01-26 07:51

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('title', models.CharField(max_length=255)),
                ('contacts', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('desc', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
            },
        ),
        migrations.CreateModel(
            name='Milestone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('title', models.PositiveSmallIntegerField()),
                ('date_start', models.DateField(blank=True, null=True)),
                ('date_finish', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Milestone',
                'verbose_name_plural': 'Milestones',
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('title', models.PositiveSmallIntegerField()),
                ('desc', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('milestone', models.ForeignKey(on_delete=None, to='pm.Milestone')),
            ],
            options={
                'verbose_name': 'Module',
                'verbose_name_plural': 'Modules',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('title', models.CharField(max_length=255)),
                ('desc', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('client', models.ForeignKey(on_delete=None, to='pm.Client')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('title', models.CharField(max_length=255)),
                ('desc', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('time', models.PositiveSmallIntegerField(default=0)),
                ('module', models.ForeignKey(on_delete=None, to='pm.Module')),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
            },
        ),
        migrations.AddField(
            model_name='milestone',
            name='project',
            field=models.ForeignKey(on_delete=None, to='pm.Project'),
        ),
    ]