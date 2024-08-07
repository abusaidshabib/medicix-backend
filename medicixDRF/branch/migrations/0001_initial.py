# Generated by Django 5.0.6 on 2024-06-26 08:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Branch",
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
                (
                    "name",
                    models.CharField(
                        max_length=250, unique=True, verbose_name="Branch Name"
                    ),
                ),
                ("branch_code", models.CharField(max_length=150, unique=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="created_branches",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BranchAddress",
            fields=[
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
                ("district", models.CharField(blank=True, max_length=150, null=True)),
                ("city", models.CharField(blank=True, max_length=150, null=True)),
                ("state", models.CharField(blank=True, max_length=150, null=True)),
                ("post_code", models.IntegerField(blank=True, null=True)),
                ("country", models.CharField(blank=True, max_length=150, null=True)),
                (
                    "branch",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="branch.branch",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
