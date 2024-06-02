# Generated by Django 5.0.6 on 2024-06-02 17:38

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

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
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("T", "Table"),
                            ("SY", "Syrups"),
                            ("SU", "Suspensions"),
                            ("IN", "Injectables"),
                            ("TO", "Topical preparations"),
                            ("D", "Drops"),
                            ("IN", "Inhalers"),
                            ("L", "Lozenges"),
                        ],
                        max_length=200,
                    ),
                ),
                ("price", models.FloatField()),
                ("use_for", models.CharField(max_length=50)),
                ("dar", models.CharField(max_length=200)),
                ("total", models.FloatField()),
                ("expire_date", models.DateField()),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
