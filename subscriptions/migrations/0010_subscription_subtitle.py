# Generated by Django 4.2.13 on 2024-07-02 07:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("subscriptions", "0009_subscription_features"),
    ]

    operations = [
        migrations.AddField(
            model_name="subscription",
            name="subtitle",
            field=models.TextField(blank=True, null=True),
        ),
    ]
