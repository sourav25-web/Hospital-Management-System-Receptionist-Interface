from django.db import models
from django.utils import timezone

class Patient(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    state = models.CharField(max_length=50)
    aadhaar_number = models.CharField(max_length=12, unique=True)
    email = models.EmailField()
    health_problem = models.TextField()
    date_of_visit = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.full_name
