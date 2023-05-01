from django.contrib import admin
from .models import Patient
# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    list_display =[ 'p_id', 'p_name', 'p_age', 'p_gender', 'p_dob', 'p_phone']
admin.site.register(Patient, PatientAdmin)