from django.db import models


class DockerAppp(models.Model):
    envs = 0
    command = 0

    name = models.CharField(max_length=255)
    image = models.CharField(max_length=1024)
    envs = models.JSONField()