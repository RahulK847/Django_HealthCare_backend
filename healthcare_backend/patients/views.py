from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Patient
from .serializers import PatientSerializer

class PatientListCreateView(generics.ListCreateAPIView):
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only return patients created by the authenticated user
        return Patient.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        # Set the authenticated user as the creator of the patient
        serializer.save(created_by=self.request.user)
    
class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only return the patient created by the authenticated user
        return Patient.objects.filter(created_by=self.request.user)