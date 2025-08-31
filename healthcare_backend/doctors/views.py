from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorListCreateView(generics.ListCreateAPIView):
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        # Return all doctors (no user filtering needed as per assignment)
        return Doctor.objects.all()

class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]
    queryset = Doctor.objects.all()