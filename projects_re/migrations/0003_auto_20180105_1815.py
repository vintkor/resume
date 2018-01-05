# Generated by Django 2.0.1 on 2018-01-05 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profile_re', '0004_auto_20180105_1754'),
        ('projects_re', '0002_remove_company_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='user',
        ),
        migrations.AddField(
            model_name='company',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='profile_re.Profile'),
            preserve_default=False,
        ),
    ]
