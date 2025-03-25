from django.contrib import admin
from .models import Patient

class PatientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'age', 'gender', 'date_of_visit')
    search_fields = ('full_name', 'phone_number', 'aadhaar_number', 'email')
    list_filter = ('gender', 'date_of_visit')
    date_hierarchy = 'date_of_visit'

admin.site.register(Patient, PatientAdmin)
