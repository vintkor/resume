# Generated by Django 2.0.1 on 2018-01-26 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pm', '0005_auto_20180126_1529'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='milestone',
            options={'ordering': ('my_order',), 'verbose_name': 'Milestone', 'verbose_name_plural': 'Milestones'},
        ),
        migrations.AlterModelOptions(
            name='module',
            options={'ordering': ('my_order',), 'verbose_name': 'Module', 'verbose_name_plural': 'Modules'},
        ),
        migrations.AddField(
            model_name='milestone',
            name='my_order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='module',
            name='my_order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
