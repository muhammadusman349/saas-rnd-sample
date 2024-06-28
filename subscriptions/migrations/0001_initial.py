# Generated by Django 4.2.13 on 2024-06-27 13:26

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Subscription",
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
                ("name", models.CharField(max_length=120)),
            ],
            options={
                "permissions": [
                    ("advanced", "Advanced Perm"),
                    ("pro", "Pro Perm"),
                    ("basic", "Basic Perm"),
                ],
            },
        ),
    ]
