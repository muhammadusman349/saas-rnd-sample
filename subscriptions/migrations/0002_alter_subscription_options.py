# Generated by Django 4.2.13 on 2024-06-27 14:01

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("subscriptions", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="subscription",
            options={
                "permissions": [
                    ("advanced", "Advanced Perm"),
                    ("pro", "Pro Perm"),
                    ("basic", "Basic Perm"),
                    ("basic_ai", "Basic_AI Perm"),
                ]
            },
        ),
    ]
