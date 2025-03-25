from django import forms
from .models import Patient
from django.utils import timezone

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            'full_name', 
            'phone_number', 
            'address', 
            'age', 
            'gender', 
            'state', 
            'aadhaar_number', 
            'email', 
            'health_problem',
            'date_of_visit'
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Full Name'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Address', 'rows': 3}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Age'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter State'}),
            'aadhaar_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Aadhaar Number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email ID'}),
            'health_problem': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Describe Health Problem', 'rows': 4}),
            'date_of_visit': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'value': timezone.now().strftime('%Y-%m-%d')})
        }
        
    def clean_aadhaar_number(self):
        aadhaar = self.cleaned_data.get('aadhaar_number')
        if not aadhaar.isdigit() or len(aadhaar) != 12:
            raise forms.ValidationError("Aadhaar number must be a 12-digit number.")
        return aadhaar
        
    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        if not phone.isdigit() or len(phone) < 10:
            raise forms.ValidationError("Please enter a valid phone number.")
        return phone 