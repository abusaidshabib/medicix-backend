from rest_framework import serializers

from .models import User, MedicineProblem
from branch.models import Branch
from medicine.models import Medicine

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = ['generic']

class MedicineProblemSerializer(serializers.ModelSerializer):
    medicine = MedicineSerializer(read_only=True)

    class Meta:
        model = MedicineProblem
        fields = ['medicine']

class UserSerializer(serializers.ModelSerializer):
    allergy = MedicineProblemSerializer(source='medicineproblem_set', many=True, read_only=True)
    class Meta:
        model = User
        fields = ['username','email','phone','address','gender','is_active','is_staff','is_admin','allergy']


class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type":"password"}, write_only=True)
    branch = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['username','email','phone','address','gender','is_active','is_staff','is_admin','branch', 'password', 'password2']
        extra_kwargs = {"password":{"write_only":True}}

    def validate(self, attrs):
        branch_name = attrs.get('branch')
        password = attrs.get('password')
        password2 = attrs.get('password2')

        if password != password2:
            raise serializers.ValidationError("Password and confirm password doesn't match")

        try:
            branch = Branch.objects.get(name=branch_name)
        except Branch.DoesNotExist:
            raise serializers.ValidationError("This is not a valid branch")

        attrs['branch'] = branch

        return attrs

    # if I create a custom model then it's need to mention create
    def create(self, validate_data):
        validate_data.pop('password2')
        return User.objects.create_user(**validate_data)