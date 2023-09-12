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
]
