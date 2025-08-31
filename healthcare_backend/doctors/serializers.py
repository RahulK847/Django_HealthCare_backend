from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Doctor
        fields = [
            'id', 'name', 'email', 'phone', 'specialization', 
            'license_number', 'experience_years', 'address', 
            'consultation_fee', 'availability', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
        
    def validate_license_number(self, value):
        """Ensure license number is unique"""
        if self.instance:
            # For updates, exclude current instance from uniqueness check
            if Doctor.objects.exclude(pk=self.instance.pk).filter(license_number=value).exists():
                raise serializers.ValidationError("A doctor with this license number already exists.")
        else:
            # For new doctors
            if Doctor.objects.filter(license_number=value).exists():
                raise serializers.ValidationError("A doctor with this license number already exists.")
        return value
    
    def validate_experience_years(self, value):
        """Ensure experience years is reasonable"""
        if value < 0:
            raise serializers.ValidationError("Experience years cannot be negative.")
        if value > 70:
            raise serializers.ValidationError("Experience years seems unrealistic.")
        return value
    
    def validate_consultation_fee(self, value):
        """Ensure consultation fee is reasonable"""
        if value < 0:
            raise serializers.ValidationError("Consultation fee cannot be negative.")
        if value > 100000:
            raise serializers.ValidationError("Consultation fee seems unrealistic.")
        return value