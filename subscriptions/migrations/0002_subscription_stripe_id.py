# Generated by Django 4.2.13 on 2024-07-01 12:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("subscriptions", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="subscription",
            name="stripe_id",
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
