# Generated by Django 5.0.4 on 2024-04-14 20:57

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField()),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField(max_length=30000)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=200)),
                ('type', models.CharField(choices=[('Part Time', 'Part Time'), ('Full Time', 'Full Time'), ('Internship', 'Internship'), ('Contract', 'Contract')], max_length=100)),
                ('education', models.CharField(choices=[('PHD', 'PHD'), ('Bachelor', 'Bachelor'), ('Master', 'Master')], max_length=100)),
                ('industry', models.CharField(choices=[('IT', 'IT'), ('Business', 'Business'), ('Video Editing', 'Video Editing')], max_length=100)),
                ('experience', models.CharField(choices=[('No Experiance', 'No Experiance'), ('Junior', 'Junior'), ('Mid Level', 'Mid Level'), ('Mid Senior', 'Mid Senior')], max_length=100)),
                ('salary', models.IntegerField()),
                ('postion', models.CharField(max_length=150)),
                ('company', models.CharField(max_length=200)),
                ('due_date', models.DateTimeField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='JobApply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField()),
                ('resume', models.CharField(max_length=300)),
                ('applied_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('cover_letter', models.TextField(max_length=500)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_jobApply', to='job.job')),
            ],
        ),
    ]
