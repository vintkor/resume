# Generated by Django 2.0.1 on 2018-01-05 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profile_re', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LanguageLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SkillLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('level', models.CharField(blank=True, choices=[('1', 'level_1'), ('2', 'level_2'), ('3', 'level_3'), ('4', 'level_4'), ('5', 'level_5'), ('6', 'level_6'), ('7', 'level_7'), ('8', 'level_8'), ('9', 'level_9'), ('10', 'level_10')], max_length=255, null=True)),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skills_re.Skill')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile_re.Profile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserLanguageLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skills_re.Language')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skills_re.LanguageLevel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile_re.Profile')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
