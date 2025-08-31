from django.db import models

class Doctor(models.Model):
    # Doctor basic information
    name = models.CharField(max_length=100)
    email = models.EmailField()  # No unique constraint like we discussed for patients
    phone = models.CharField(max_length=15)
    
    # Professional information
    specialization = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50, unique=True)
    experience_years = models.PositiveIntegerField()
    
    # Contact information
    address = models.TextField()
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Availability
    availability = models.CharField(
        max_length=200,
        help_text="e.g., Mon-Fri 9AM-5PM"
    )
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return f"Dr. {self.name} - {self.specialization}"