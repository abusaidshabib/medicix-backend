# Generated by Django 5.0.6 on 2024-06-26 08:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("branch", "0001_initial"),
        ("content", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Medicine",
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
                ("brand", models.CharField(max_length=200)),
                ("manufacturer", models.CharField(max_length=255)),
                ("generic", models.CharField(max_length=150)),
                ("strength", models.CharField(max_length=150)),
                ("price", models.FloatField()),
                ("use_for", models.CharField(max_length=50)),
                ("dar", models.CharField(max_length=200)),
                ("total", models.FloatField()),
                (
                    "subcategory",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="medicines",
                        to="content.subcategory",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Inventory",
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
                ("quantity", models.IntegerField()),
                ("soled", models.IntegerField()),
                ("expire_date", models.DateField()),
                (
                    "branch",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="branch.branch",
                        verbose_name="Branch",
                    ),
                ),
                (
                    "medicine",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="inventories",
                        to="medicine.medicine",
                        verbose_name="Medicine",
                    ),
                ),
            ],
            options={
                "unique_together": {("medicine", "branch")},
            },
        ),
    ]
