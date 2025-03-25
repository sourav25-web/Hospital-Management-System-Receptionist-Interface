from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Patient
from .forms import PatientForm

def patient_register(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Patient registered successfully!")
            return redirect('patient_list')
    else:
        form = PatientForm()
    
    return render(request, 'receptionist/patient_register.html', {'form': form, 'title': 'Register Patient'})

def patient_list(request):
    patients = Patient.objects.all().order_by('-created_at')
    return render(request, 'receptionist/patient_list.html', {'patients': patients, 'title': 'Patient List'})

def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    return render(request, 'receptionist/patient_detail.html', {'patient': patient, 'title': 'Patient Detail'})

def home(request):
    return render(request, 'receptionist/home.html', {'title': 'Hospital Management System'})
