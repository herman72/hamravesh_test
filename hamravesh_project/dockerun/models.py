from django.db import models


class DockerApp(models.Model):

    name = models.CharField(max_length=255)
    image = models.CharField(max_length=1024)
    envs = models.JSONField()
    command = models.CharField(max_length=1024)
    status = models.BooleanField(default=False)

class ExecutionApp(models.Model):

    app = models.ForeignKey(DockerApp, on_delete=models.SET_NULL)
    run_at = models.DateTimeField(auto_now_add=True)
    run_params = models.JSONField()
    is_running = models.BooleanField()