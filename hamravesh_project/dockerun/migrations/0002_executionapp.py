# Generated by Django 4.1.4 on 2022-12-10 23:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("dockerun", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ExecutionApp",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("run_at", models.DateTimeField(auto_now_add=True)),
                ("run_params", models.JSONField()),
                ("is_running", models.BooleanField()),
                ("created_container_id", models.CharField(max_length=50)),
                (
                    "app",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="dockerun.dockerapp",
                    ),
                ),
            ],
        ),
    ]