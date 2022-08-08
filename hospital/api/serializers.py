from rest_framework import serializers
from api.models import Patient,Department,Doctor
from django.contrib.auth.models import User


class DepartmentSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        id=serializers.CharField(read_only=True)
        model=Department
        # fields=['id','Name','Department_head']
        fields = '__all__'
class DoctorSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=Doctor
        fields=['id','Name','Department','Contact_number']


class PatientSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=Patient
        fields=['id','Name','Department','contact_number','Doctor']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','first_name','last_name','username','email','password']
    def create(self,validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()



