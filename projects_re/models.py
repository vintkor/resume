from django.db import models
from resume.basemodel import AbstractDateModel
from profile_re.models import Profile
from ckeditor_uploader.fields import RichTextUploadingField


class Company(AbstractDateModel):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    date_start = models.DateField()
    date_finish = models.DateField(blank=True, null=True)
    position = models.CharField(max_length=255)
    description = RichTextUploadingField()

    def __str__(self):
        return '{} {}'.format(self.title, self.user)


class Project(AbstractDateModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = RichTextUploadingField()

    def __str__(self):
        return '{} {} {}'.format(self.company.user, self.company, self.title)
