# Generated by Django 4.2.5 on 2023-09-12 11:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("appointment", "0004_doctor_password"),
    ]

    operations = [
        migrations.AlterField(
            model_name="doctor",
            name="password",
            field=models.CharField(default="12345", max_length=128, null=True),
        ),
    ]
