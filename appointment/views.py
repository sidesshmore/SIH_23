# views.py

from rest_framework import generics
from .models import Hospital, Category, Doctor, Slot, Patient, Attendance
from .serializers import HospitalSerializer, CategorySerializer, DoctorSerializer, SlotSerializer, PatientSerializer, AttendanceSerializer

class HospitalListCreateView(generics.ListCreateAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class DoctorListCreateView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class SlotListCreateView(generics.ListCreateAPIView):
    queryset = Slot.objects.all()
    serializer_class = SlotSerializer

class PatientListCreateView(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class AttendanceListCreateView(generics.ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer


from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import Hospital, Category, Doctor, Slot
from .serializers import HospitalSerializer, CategorySerializer, DoctorSerializer, SlotSerializer

class HospitalDetailView(generics.RetrieveAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
    lookup_field = 'hospital_id'

class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'


# views.py

from rest_framework.response import Response

class CategoryDoctorsWithFreeSlotsView(generics.RetrieveAPIView):
    serializer_class = DoctorSerializer

    def retrieve(self, request, hospital_id, pk):
        # Get the hospital and category
        hospital = get_object_or_404(Hospital, hospital_id=hospital_id)
        category = get_object_or_404(Category, pk=pk)

        # Get doctors in the category
        doctors = Doctor.objects.filter(hospital=hospital, categories=category)

        # Filter doctors with free slots
        doctors_with_free_slots = []
        for doctor in doctors:
            free_slots = Slot.objects.filter(doctor=doctor, status=True)
            if free_slots.exists():
                doctors_with_free_slots.append(doctor)

        serializer = self.get_serializer(doctors_with_free_slots, many=True)
        return Response(serializer.data)



from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Hospital, Category, Doctor, Slot
from .serializers import DoctorSerializer, SlotSerializer

@api_view(['GET'])
def category_doctors(request, hospital_id, category_id):
    try:
        hospital = Hospital.objects.get(hospital_id=hospital_id)
        category = Category.objects.get(id=category_id, hospital=hospital)
        doctors = Doctor.objects.filter(hospital=hospital, categories=category)
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)
    except Hospital.DoesNotExist:
        return Response({"message": "Hospital not found"}, status=404)
    except Category.DoesNotExist:
        return Response({"message": "Category not found for this hospital"}, status=404)

@api_view(['GET'])
def doctor_slots(request, hospital_id, category_id, doctor_id):
    try:
        hospital = Hospital.objects.get(hospital_id=hospital_id)
        category = Category.objects.get(id=category_id, hospital=hospital)
        doctor = Doctor.objects.get(doctor_id=doctor_id, hospital=hospital)
        slots = Slot.objects.filter(doctor=doctor, status=True)
        serializer = SlotSerializer(slots, many=True)
        return Response(serializer.data)
    except Hospital.DoesNotExist:
        return Response({"message": "Hospital not found"}, status=404)
    except Category.DoesNotExist:
        return Response({"message": "Category not found for this hospital"}, status=404)
    except Doctor.DoesNotExist:
        return Response({"message": "Doctor not found for this hospital"}, status=404)

    
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from .models import Doctor, Category, PatientAllocation
from .serializers import PatientAllocationSerializer

@api_view(['POST'])
def allocate_doctor_and_update_waitlist(request):
    # Extract data from the request
    patient_name = request.data.get('patient_name')
    category_id = request.data.get('category_id')

    try:
        # Get the category name for the given category_id
        category = Category.objects.get(pk=category_id)
        category_name = category.name
    except Category.DoesNotExist:
        return Response({"message": "Invalid category_id"}, status=HTTP_400_BAD_REQUEST)

    try:
        # Get relevant doctors for the specified category
        relevant_doctors = Doctor.objects.filter(categories__id=category_id, present=True)

        if not relevant_doctors.exists():
            return Response({"message": "No available doctors for the specified category."}, status=HTTP_400_BAD_REQUEST)

        # Find the doctor with the minimum waitlist count
        allocated_doctor = relevant_doctors.order_by('waitlist_count').first()
        allocated_doctor_id = allocated_doctor.doctor_id
        allocated_category_id = category_id

        # Update waitlist count for the allocated doctor
        allocated_doctor.waitlist_count += 1
        allocated_doctor.save()

        # Create a patient allocation record
        allocation_data = {
            "doctor_id": allocated_doctor_id,
            "patient_name": patient_name,
            "attended": "Pending",
            "category_id": allocated_category_id
        }

        allocation_serializer = PatientAllocationSerializer(data=allocation_data)
        if allocation_serializer.is_valid():
            allocation_serializer.save()

        return Response({
            "allocated_doctor_id": allocated_doctor_id,
            "allocated_doctor_category_id": allocated_category_id
        })
    except Exception as e:
        return Response({"message": str(e)}, status=HTTP_400_BAD_REQUEST)
    
from django.http import JsonResponse
from .models import PatientAllocation

def get_doctor_appointments(request, doctor_id):
    # Retrieve the patients for the given doctor_id
    doctor_patients = PatientAllocation.objects.filter(doctor_id=doctor_id)
    patients_list = list(doctor_patients.values_list('patient_name', flat=True))
    return JsonResponse({"patients": patients_list})

import pandas as pd
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import PatientAllocation

@api_view(['POST'])
def remove_patient_by_name(request):
    patient_name = request.data.get('patient_name')

    # Remove the patient record based on the patient name
    PatientAllocation.objects.filter(patient_name=patient_name).delete()

    message = f"Patient with name '{patient_name}' removed successfully."
    return Response({"message": message}, status=200)





