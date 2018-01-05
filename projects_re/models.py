from django.db import models
from resume.basemodel import AbstractDateModel
from profile_re.models import Profile


class Company(AbstractDateModel):
    title = models.CharField(max_length=200)
    date_start = models.DateField()
    date_finish = models.DateField(blank=True, null=True)
    position = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class Project(AbstractDateModel):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return '{} {}'.format(self.user, self.title)
