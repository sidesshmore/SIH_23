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

