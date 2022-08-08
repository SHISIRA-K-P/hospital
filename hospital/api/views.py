# Create your views here.
import json
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers import *
from api.models import Department, Doctor, Patient
from django.contrib.auth import authenticate,login
from rest_framework import authentication,permissions


class PatientView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def get(self,request,*args,**kwargs):
        patient_obj=Patient.objects.all()
        serializer=PatientSerializer(patient_obj,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request,*args,**kwargs):
        serializer=PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class PatientDetailView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        patient_obj=Patient.objects.get(id=id)
        serializer=PatientSerializer(patient_obj)
        return Response(serializer.data)
    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        patient_obj=Patient.objects.get(id=id)
        serializer=PatientSerializer(instance=patient_obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        patient_obj=Patient.objects.get(id=id)
        patient_obj.delete()
        return Response({"msg":"deleted"})



class DepartmentView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def get(self,request,*args,**kwargs):
        qs=Department.objects.all()
        serializer=DepartmentSerializer(qs,many=True)
        return Response(serializer.data)
    
    def post(self,request,*args,**kwargs):
        serializer=DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


class DepartmentDetailView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        dept=Department.objects.get(id=id)
        serializer=DepartmentSerializer(dept)
        return Response(serializer.data)
    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        dept=Department.objects.get(id=id)
        serializer=DepartmentSerializer(instance=dept,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        dept=Department.objects.get(id=id)
        dept.delete()
        return Response({"msg":"deleted"})

class DoctorView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def get(self,request,*args,**kwargs):
        dr=Doctor.objects.all()
        serializer=DoctorSerializer(dr,many=True)
        return Response(serializer.data)
    
    def post(self,request,*args,**kwargs):
        serializer=DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


class DoctorDetailView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        dr=Doctor.objects.get(id=id)
        serializer=DoctorSerializer(dr)
        return Response(serializer.data)
    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        dr=Doctor.objects.get(id=id)
        serializer=DoctorSerializer(instance=dr,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        dr=Doctor.objects.get(id=id)
        dr.delete()
        return Response({"msg":"deleted"})


# api/v1/user/accounts/signin

class UserCreationView(APIView):
    def post(self,request,*args,**kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response({"msg":"success"},status=status.HTTP_201_CREATED)
        else:
            return Response({"msg":"not success"},status=status.HTTP_401_UNAUTHORIZED)

class SignInView(APIView):
    def post(self,request,*args,**kwargs):
        serializer=LoginSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            uname=serializer.validated_data.get("username")
            print(uname)
            password=serializer.validated_data.get("password")
            print(password)
            user=authenticate(request,username=uname,password=password)
            print(user)
            if user:
                login(request,user)
                return Response({"msg":"success"})
            else:
                return Response({"msg":"Invalid credetials"})



        