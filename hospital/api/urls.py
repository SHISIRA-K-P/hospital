from django.contrib import admin
from .views import PatientDetailView,PatientView,DepartmentView,DepartmentDetailView,DoctorView,DoctorDetailView,SignInView,UserCreationView
from django.urls import include, path

urlpatterns = [
    path('patient',PatientView.as_view()),
    path('patient/<int:id>',PatientDetailView.as_view()),
    path('department',DepartmentView.as_view()),
    path('department/<int:id>',DepartmentDetailView.as_view()),
    path('doctor',DoctorView.as_view()),
    path('doctor/<int:id>',DoctorDetailView.as_view()),
    path("users/accounts/signup",UserCreationView.as_view()),
    path("users/accounts/login",SignInView.as_view())

]
