# Generated by Django 4.2.5 on 2023-09-12 10:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("appointment", "0003_slot_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="doctor",
            name="password",
            field=models.CharField(max_length=128, null=True),
        ),
    ]
