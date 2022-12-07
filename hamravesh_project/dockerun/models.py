from django.db import models


class DockerApp(models.Model):

    name = models.CharField(max_length=255)
    image = models.CharField(max_length=1024)
    envs = models.JSONField()
    command = models.CharField(max_length=1024)
    status = models.BooleanField(default=False)
