# admin.py

from django.contrib import admin
from .models import Hospital, Category, Doctor, Slot, Patient, Attendance

class HospitalAdmin(admin.ModelAdmin):
    list_display = ('hospital_id', 'name', 'address', 'phone')
    list_display_links = ['hospital_id']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('doctor_id', 'doctor_name', 'degree', 'phone', 'hospital')
    list_display_links = ['doctor_id']

class SlotAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'end_time', 'doctor', 'status')
    list_display_links = ['start_time', 'end_time']

class PatientAdmin(admin.ModelAdmin):
    sortable_by = 'uid'
    search_fields = ['uid', 'name', 'email']
    list_display = ('uid', 'name', 'dob', 'email', 'phone', 'gender')
    list_display_links = ['uid']

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('entry_time', 'exit_time', 'doctor')
    list_display_links = ['entry_time', 'exit_time']

admin.site.register(Hospital, HospitalAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Slot, SlotAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Attendance, AttendanceAdmin)
