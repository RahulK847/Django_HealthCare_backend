from rest_framework import serializers
from .models import PatientDoctorMapping
from patients.models import Patient
from doctors.models import Doctor
from patients.serializers import PatientSerializer
from doctors.serializers import DoctorSerializer

class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
    patient_details = PatientSerializer(source='patient', read_only=True)
    doctor_details = DoctorSerializer(source='doctor', read_only=True)
    
    class Meta:
        model = PatientDoctorMapping
        fields = [
            'id', 'patient', 'doctor', 'patient_details', 'doctor_details',
            'notes', 'is_active', 'assigned_date', 'created_by', 
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_by', 'assigned_date', 'created_at', 'updated_at']
    
    def validate(self, data):
        """Custom validation for patient-doctor mapping"""
        patient = data.get('patient')
        doctor = data.get('doctor')
        request = self.context.get('request')
        
        # Ensure the patient belongs to the authenticated user
        if patient and patient.created_by != request.user:
            raise serializers.ValidationError(
                "You can only assign doctors to patients you created."
            )
        
        # Check if mapping already exists (for create operations)
        if not self.instance:  # Creating new mapping
            if PatientDoctorMapping.objects.filter(
                patient=patient, 
                doctor=doctor, 
                is_active=True
            ).exists():
                raise serializers.ValidationError(
                    "This patient is already assigned to this doctor."
                )
        
        return data

class PatientDoctorMappingCreateSerializer(serializers.ModelSerializer):
    """Simplified serializer for creating mappings"""
    
    class Meta:
        model = PatientDoctorMapping
        fields = ['patient', 'doctor', 'notes']
    
    def validate(self, data):
        """Custom validation for patient-doctor mapping"""
        patient = data.get('patient')
        doctor = data.get('doctor')
        request = self.context.get('request')
        
        # Ensure the patient belongs to the authenticated user
        if patient and patient.created_by != request.user:
            raise serializers.ValidationError(
                "You can only assign doctors to patients you created."
            )
        
        # Check if mapping already exists
        if PatientDoctorMapping.objects.filter(
            patient=patient, 
            doctor=doctor, 
            is_active=True
        ).exists():
            raise serializers.ValidationError(
                "This patient is already assigned to this doctor."
            )
        
        return data