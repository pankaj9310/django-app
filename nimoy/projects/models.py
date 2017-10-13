from __future__ import unicode_literals

from django.db import models
from django.conf import settings
# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=160)
    description = models.TextField()
    project_type = models.CharField(null=True, max_length=160)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='projects', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class ProjectMember(models.Model):
    member = models.ForeignKey(settings.AUTH_USER_MODEL)
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='projects'
    )