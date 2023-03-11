from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

CHOICES = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
    ('Internship', 'Internship'),
    ('Remote', 'Remote'),
)


class Job(models.Model):
    recruiter = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='jobs')
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=255)
    description = models.TextField()
    skills_req = models.CharField(max_length=200)
    job_type = models.CharField(
        max_length=30, choices=CHOICES, default='Full Time', null=True)
    link = models.URLField(null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return self.title


class Applicants(models.Model):
    job = models.ForeignKey(
        Job, related_name='applicants', on_delete=models.CASCADE)
    applicant = models.ForeignKey(
        User, related_name='applied', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.applicant


class Selected(models.Model):
    job = models.ForeignKey(
        Job, related_name='select_job', on_delete=models.CASCADE)
    applicant = models.ForeignKey(
        User, related_name='select_applicant', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.applicant
