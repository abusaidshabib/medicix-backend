# Generated by Django 5.0.6 on 2024-06-02 19:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authentication", "0002_alter_myuser_branch"),
        ("branch", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="myuser",
            name="branch",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="branch.branch",
                verbose_name="user branch",
            ),
        ),
    ]
