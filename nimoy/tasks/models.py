from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from nimoy.projects.models import Project
# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    assignee = models.ForeignKey(settings.AUTH_USER_MODEL)
    task_type = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='tasks',
                              on_delete=models.CASCADE)
    priority = models.CharField(max_length=50, blank=True, null=True)
    due = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='tasks'
    )

    def __str__(self):
        if self.name:
            return self.name
