from django.urls import path
from . import views
urlpatterns = [
    path('ad/', views.addPatientView, name = 'addpatient_url' ),
    path('sh/', views.showPatientView, name="showpatient_url"),
    path('up/<int:pk>/', views.updatePatientView, name="updatepatient_url"),
    path('dl/<int:pk>/', views.deletePatientView, name="deletepatient_url"),
    
    
    
]
