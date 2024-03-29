# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('hospitals/', views.HospitalListCreateView.as_view(), name='hospital-list-create'),
    path('categories/', views.CategoryListCreateView.as_view(), name='category-list-create'),
    path('doctors/', views.DoctorListCreateView.as_view(), name='doctor-list-create'),
    path('slots/', views.SlotListCreateView.as_view(), name='slot-list-create'),
    path('patients/', views.PatientListCreateView.as_view(), name='patient-list-create'),
    path('attendance/', views.AttendanceListCreateView.as_view(), name='attendance-list-create'),
    path('hospital/<str:hospital_id>/', views.HospitalDetailView.as_view(), name='hospital-detail'),
    path('hospital/<str:hospital_id>/category/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),
    path('hospital/<str:hospital_id>/category/<int:category_id>/doctor/<str:doctor_id>/slots/', views.doctor_slots, name='doctor-slots'),
    path('doctor_app/<str:doctor_id>/', views.get_doctor_appointments, name='get_doctor_appointments'),
    path('allocate_doctor/', views.allocate_doctor_and_update_waitlist, name='allocate_doctor'),
    path('remove_patient/', views.remove_patient_by_name, name='remove_patient_by_name'),
]

