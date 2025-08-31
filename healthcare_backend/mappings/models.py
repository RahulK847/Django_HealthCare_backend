from django.db import models
from django.conf import settings
from patients.models import Patient
from doctors.models import Doctor

class PatientDoctorMapping(models.Model):
    # The user who created this mapping
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='created_mappings'
    )
    
    # Patient and Doctor relationship
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='doctor_mappings'
    )
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name='patient_mappings'
    )
    
    # Assignment details
    assigned_date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True, help_text="Assignment notes or reason")
    is_active = models.BooleanField(default=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        # Prevent duplicate mappings for the same patient-doctor pair
        unique_together = ['patient', 'doctor']
        ordering = ['-assigned_date']
    
    def __str__(self):
        return f"{self.patient.name} → Dr. {self.doctor.name}"