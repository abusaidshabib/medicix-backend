# Generated by Django 5.0.6 on 2024-06-16 09:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("branch", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="BranchAddress",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "house_number",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                (
                    "holding_number",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                (
                    "street_name",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                ("village", models.CharField(blank=True, max_length=150, null=True)),
                (
                    "post_office",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                ("city", models.CharField(blank=True, max_length=150, null=True)),
                ("state", models.CharField(blank=True, max_length=150, null=True)),
                ("post_code", models.IntegerField(blank=True, null=True)),
                ("district", models.CharField(blank=True, max_length=150, null=True)),
                ("country", models.CharField(blank=True, max_length=150, null=True)),
                (
                    "branch",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="branch.branch",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
