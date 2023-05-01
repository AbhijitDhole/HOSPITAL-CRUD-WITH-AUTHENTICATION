from django.shortcuts import render, redirect
from .models import Patient
from .forms import PatientForm
# Create your views here.


def addPatientView(request):
    form = PatientForm()
    template_name = "crudapp2/add.html"
    context = {'form': form}
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, template_name, context)

def showPatientView(request):
    data = Patient.objects.all()
    template_name = 'crudapp2/show.html'
    context = {'obj': data}
    return render(request, template_name, context)

def updatePatientView(request, pk):
    data = Patient.objects.get(id = pk)
    form = PatientForm(instance=data)
    template_name = "crudapp2/add.html"
    context = {"form": form}
    if request.method == "POST":
        form = PatientForm(request.POST, instance= data)
        if form.is_valid():
            form.save()
            return redirect('showpatient_url')
    return render(request, template_name, context)

def deletePatientView(request, pk):
    ord = Patient.objects.get(id = pk)
    template_name = "crudapp2/confirm.html"
    context = {'obj': ord}
    if request.method == "POST":
        ord.delete()
        return redirect('showpatient_url')
    return render(request, template_name, context)
      