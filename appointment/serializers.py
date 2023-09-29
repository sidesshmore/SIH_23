# serializers.py

from rest_framework import serializers
from .models import Hospital, Category, Doctor, Slot, Patient, Attendance

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slot
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

from rest_framework import serializers
from .models import PatientAllocation, PatientCategoryPreference

class PatientAllocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientAllocation
        fields = '__all__'

class PatientCategoryPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientCategoryPreference
        fields = '__all__'
