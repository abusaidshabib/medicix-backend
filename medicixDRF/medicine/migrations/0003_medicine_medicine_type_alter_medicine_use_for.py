# Generated by Django 5.0.6 on 2024-06-26 10:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("medicine", "0002_remove_medicine_total"),
    ]

    operations = [
        migrations.AddField(
            model_name="medicine",
            name="medicine_type",
            field=models.CharField(
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
                default=0,
                max_length=50,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="medicine",
            name="use_for",
            field=models.CharField(
                choices=[("H", "Human"), ("A", "Animal")], max_length=50
            ),
        ),
    ]