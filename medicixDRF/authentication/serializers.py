from rest_framework import serializers

from .models import MyUser, MedicineProblem
from medicine.serializers import MedicineSerializer

class MedicineProblemSerializer(serializers.ModelSerializer):
    medicine = MedicineSerializer(read_only=True)

    class Meta:
        model = MedicineProblem
        fields = ['medicine']

class MyUserSerializer(serializers.ModelSerializer):
    allergy = MedicineProblemSerializer(source='medicineproblem_set', many=True, read_only=True)
    class Meta:
        model = MyUser
        fields = ['username','email','phone','address','dob','gender','is_active','is_staff','is_admin','allergy']