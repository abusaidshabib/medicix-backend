# Generated by Django 5.0.6 on 2024-06-26 10:03

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("medicine", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="medicine",
            name="total",
        ),
    ]
