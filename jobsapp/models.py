from django.db import models
from django.utils import timezone

from accounts.models import User

JOB_TYPE = (
    ('1', "Full time"),
    ('2', "Part time"),
    ('3', "Internship"),
)


class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    description = models.TextField()
    location = models.CharField(max_length=150)
    type = models.CharField(choices=JOB_TYPE, max_length=10)
    category = models.CharField(max_length=100)
    last_date = models.DateTimeField()
    company_name = models.CharField(max_length=100)
    company_description = models.TextField()
    website = models.CharField(max_length=100, default="")
    created_at = models.DateTimeField(default=timezone.now)
    filled = models.BooleanField(default=False)
    salary = models.CharField(max_length=100, default="", null=True, blank=True)
    vacant = models.CharField(max_length=100, default="", null=False, blank=False)

    def __str__(self):
        return self.title


class Applicant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applicants')
    created_at = models.DateTimeField(default=timezone.now)
    fullname = models.CharField(max_length=50, default="")
    education = models.CharField(max_length=500, default="", null=True, blank=True)
    skills = models.CharField(max_length=500, default="", null=True, blank=True)
    former_job = models.CharField(max_length=500, default="", null=True, blank=True)
    eligibility = models.CharField(max_length=500, default="", null=True, blank=True)
    experience = models.CharField(max_length=500, default="", null=True, blank=True)
    coverletter = models.TextField(default="")


    def __str__(self):
        return self.user.get_full_name()