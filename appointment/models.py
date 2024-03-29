# models.py
from django.db import models

class Hospital(models.Model):
    hospital_id = models.CharField(primary_key=True, max_length=9)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    categories = models.ManyToManyField('Category')

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    doctor_id = models.CharField(primary_key=True, max_length=9)
    doctor_name = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    password = models.CharField(max_length=128, null=True, default= '12345')  
    present = models.BooleanField(default=True)
    waitlist_count = models.IntegerField(default=0)

    def __str__(self):
        return self.doctor_name

class Patient(models.Model):
    uid = models.CharField(primary_key=True, max_length=12)
    name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=1)  # Assuming 'M' or 'F' for Male/Female
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    street = models.CharField(max_length=100)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)
    otp = models.CharField(max_length=4, null=True, blank=True)

    def __str__(self):
        return self.name



class Slot(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    status = models.BooleanField(default=True)  # True for free, False for booked
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True, blank=True)  # Link to Patient
    status = models.CharField(max_length=20, default='Available')  # Status of the slot: Available/Booked

    def __str__(self):
        return f'{self.start_time} - {self.end_time}'





class Attendance(models.Model):
    # entry_time = models.DateTimeField()
    # exit_time = models.DateTimeField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    present = models.BooleanField(default=False) 

    def __str__(self):
        return f'{self.doctor} ({self.entry_time} - {self.exit_time})'


class PatientAllocation(models.Model):
    doctor_id = models.CharField(max_length=9)
    patient_name = models.CharField(max_length=100)
    attended = models.CharField(max_length=50)
    category_id = models.IntegerField()

    def __str__(self):
        return f'{self.patient_name} allocated to {self.doctor_id}'

class PatientCategoryPreference(models.Model):
    patient_name = models.CharField(max_length=100)
    category_id = models.IntegerField()

    def __str__(self):
        return f'{self.patient_name} prefers category {self.category_id}'