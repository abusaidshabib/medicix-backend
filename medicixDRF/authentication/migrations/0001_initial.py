# Generated by Django 5.0.6 on 2024-06-24 08:39

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("username", models.CharField(blank=True, max_length=150, null=True)),
                ("email", models.EmailField(max_length=200, unique=True)),
                ("phone", models.CharField(max_length=50)),
                ("address", models.CharField(max_length=255)),
                ("is_active", models.BooleanField(default=True)),
                ("is_staff", models.BooleanField(default=False)),
                ("is_admin", models.BooleanField(default=False)),
                ("is_superuser", models.BooleanField(default=False)),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female"), ("T", "Trans")],
                        max_length=50,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="MedicineProblem",
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
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="UserDetails",
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
                ("district", models.CharField(blank=True, max_length=150, null=True)),
                ("city", models.CharField(blank=True, max_length=150, null=True)),
                ("state", models.CharField(blank=True, max_length=150, null=True)),
                ("post_code", models.IntegerField(blank=True, null=True)),
                ("country", models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
