from django.db import models
from django.utils import timezone

JOB_TYPE =(
    ('Part Time','Part Time'),
    ('Full Time','Full Time'),
    ('Internship','Internship'),
    ('Contract','Contract'),
)

JOB_EDUCATION=(
    ('PHD','PHD'),
    ('Bachelor','Bachelor'),
    ('Master','Master'),
)
JOB_INDUSTRY = (
    ('IT','IT'),
    ('Business','Business'),
    ('Video Editing','Video Editing'),
)

JOB_EXPERIENCE = (
    ('No Experiance','No Experiance'),
    ('Junior','Junior'),
    ('Mid Level','Mid Level'),
    ('Mid Senior','Mid Senior'),
)

class Job(models.Model):
    user = models.IntegerField()
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=30000)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=200)
    type = models.CharField(max_length=100,choices=JOB_TYPE)
    education = models.CharField(max_length=100,choices=JOB_EDUCATION)
    industry = models.CharField(max_length=100,choices=JOB_INDUSTRY)
    experience = models.CharField(max_length=100,choices=JOB_EXPERIENCE)
    salary = models.IntegerField()
    postion = models.CharField(max_length=150)
    company = models.CharField(max_length=200)
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title

class JobApply(models.Model):
    user = models.IntegerField()
    job = models.ForeignKey(Job,related_name='job_jobApply',on_delete=models.CASCADE)
    resume = models.CharField(max_length=300)
    applied_at = models.DateTimeField(default=timezone.now)
    cover_letter = models.TextField(max_length=500)
    
    def __str__(self):
        return str(self.job)