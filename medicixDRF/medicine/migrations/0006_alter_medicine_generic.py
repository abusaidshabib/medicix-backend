# Generated by Django 5.0.6 on 2024-07-13 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("medicine", "0005_alter_medicine_use_for"),
    ]

    operations = [
        migrations.AlterField(
            model_name="medicine",
            name="generic",
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
