from rest_framework import serializers

from .models import MyUser, MedicineProblem
from branch.models import Branch
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


class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={"input_type":"password"}, write_only=True)
    branch = serializers.CharField(required=True)

    class Meta:
        model = MyUser
        fields = ['username','email','phone','address','dob','gender','is_active','is_staff','is_admin','branch', 'confirm_password', 'password']
        extra_kwargs = {"password":{"write_only":True}}

    def create(self, validated_data):
        password = validated_data["password"]
        confirm_password = validated_data["confirm_password"]
        if password != confirm_password:
            raise serializers.ValidationError({"password":"Password must match"})
        branch_id = validated_data.pop('branch')
        try:
            branch = Branch.objects.get(pk=branch_id)
        except Branch.DoesNotExist:
            raise serializers.ValidationError({"branch":"Invalid branch ID."})
        user = MyUser(**validated_data)
        user.set_password(password)
        user.branch = branch
        user.save()
        return user

