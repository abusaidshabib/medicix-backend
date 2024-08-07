# Generated by Django 5.0.6 on 2024-06-26 08:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("authentication", "0001_initial"),
        ("branch", "0001_initial"),
        ("medicine", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="branch",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="branch.branch",
                verbose_name="user branch",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="medicineproblem",
            name="medicine",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="medicine.medicine",
                verbose_name="name_of_medicine",
            ),
        ),
        migrations.AddField(
            model_name="medicineproblem",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="allergic_customers",
            ),
        ),
    ]
