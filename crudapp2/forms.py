from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"
        labels = {
            'p_id':'PATIENT ID',
            'p_name':'NAME',
            'p_age':'AGE',
            'p_dob':'DATE OF BIRTH',
            'p_gender':'GENDER',
            'p_phone':'PHONE NUMBER',
            
        }
        widgets = {
            'p_dob': forms.DateInput(attrs ={'type':'date'})
        }