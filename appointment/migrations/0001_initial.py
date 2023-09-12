# Generated by Django 4.2.5 on 2023-09-11 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Doctor",
            fields=[
                (
                    "doctor_id",
                    models.CharField(max_length=9, primary_key=True, serialize=False),
                ),
                ("doctor_name", models.CharField(max_length=100)),
                ("degree", models.CharField(max_length=100)),
                ("doctor_number", models.CharField(max_length=15)),
                ("categories", models.ManyToManyField(to="appointment.category")),
            ],
        ),
        migrations.CreateModel(
            name="Patient",
            fields=[
                (
                    "uid",
                    models.CharField(max_length=12, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=100)),
                ("dob", models.DateField()),
                ("gender", models.CharField(max_length=1)),
                ("phone", models.CharField(max_length=10)),
                ("email", models.EmailField(max_length=254)),
                ("street", models.CharField(max_length=100)),
                ("district", models.CharField(max_length=50)),
                ("state", models.CharField(max_length=50)),
                ("pincode", models.CharField(max_length=6)),
                ("otp", models.CharField(blank=True, max_length=4, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Slot",
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
                ("start_time", models.TimeField()),
                ("end_time", models.TimeField()),
                ("status", models.BooleanField(default=True)),
                (
                    "doctor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="appointment.doctor",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Hospital",
            fields=[
                (
                    "hospital_id",
                    models.CharField(max_length=9, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=100)),
                ("address", models.CharField(max_length=200)),
                ("phone", models.CharField(max_length=15)),
                ("categories", models.ManyToManyField(to="appointment.category")),
            ],
        ),
        migrations.AddField(
            model_name="doctor",
            name="hospital",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="appointment.hospital"
            ),
        ),
        migrations.CreateModel(
            name="Attendance",
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
                ("entry_time", models.DateTimeField()),
                ("exit_time", models.DateTimeField()),
                (
                    "doctor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="appointment.doctor",
                    ),
                ),
            ],
        ),
    ]