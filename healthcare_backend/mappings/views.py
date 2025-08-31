from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import PatientDoctorMapping
from .serializers import PatientDoctorMappingSerializer, PatientDoctorMappingCreateSerializer
from patients.models import Patient

class MappingListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PatientDoctorMappingCreateSerializer
        return PatientDoctorMappingSerializer
    
    def get_queryset(self):
        # Return only mappings for patients created by the authenticated user
        return PatientDoctorMapping.objects.filter(
            patient__created_by=self.request.user,
            is_active=True
        )
    
    def perform_create(self, serializer):
        # Set the authenticated user as the creator
        serializer.save(created_by=self.request.user)

class MappingDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        # Return only mappings for patients created by the authenticated user
        return PatientDoctorMapping.objects.filter(
            patient__created_by=self.request.user
        )
    
    def destroy(self, request, *args, **kwargs):
        mapping = self.get_object()
        # Soft delete by setting is_active to False
        mapping.is_active = False
        mapping.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PatientDoctorsView(generics.ListAPIView):
    """Get all doctors assigned to a specific patient"""
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        patient_id = self.kwargs['patient_id']
        # Ensure the patient belongs to the authenticated user
        patient = get_object_or_404(
            Patient, 
            id=patient_id, 
            created_by=self.request.user
        )
        return PatientDoctorMapping.objects.filter(
            patient=patient,
            is_active=True
        )