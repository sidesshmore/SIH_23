# Generated by Django 4.2.5 on 2023-09-25 10:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("appointment", "0006_slot_patient"),
    ]

    operations = [
        migrations.AddField(
            model_name="attendance",
            name="present",
            field=models.BooleanField(default=False),
        ),
    ]
