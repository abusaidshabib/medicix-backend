from rest_framework import serializers

from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from .utils import Util
from drf_extra_fields.fields import Base64ImageField

from .models import User, MedicineProblem, UserDetails
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

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ["house_number", "holding_number", "street_name", "village", "post_office", "district", "city", "state", "post_code", "country"]

class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type":"password"}, write_only=True)
    branch = serializers.CharField(required=True)
    created_by = serializers.EmailField(write_only=True)
    userdetails = UserDetailsSerializer(required=True)

    class Meta:
        model = User
        fields = ['username','email','phone','address','gender','is_active','is_staff','is_admin','branch', 'password', 'password2','created_by','userdetails']
        extra_kwargs = {"password":{"write_only":True}}

    def validate(self, attrs):
        branch_name = attrs.get('branch')
        password = attrs.get('password')
        password2 = attrs.get('password2')
        created_by = attrs.get('created_by')

        if password != password2:
            raise serializers.ValidationError("Password and confirm password doesn't match")

        try:
            branch = Branch.objects.get(name=branch_name)
        except Branch.DoesNotExist:
            raise serializers.ValidationError("This is not a valid branch")

        try:
            created_by = User.objects.get(email=created_by)
        except User.DoesNotExist:
            raise serializers.ValidationError("This is not a valid user")

        attrs['branch'] = branch
        attrs['created_by'] = created_by

        return attrs

    # if I create a custom model then it's need to mention create
    def create(self, validate_data):
        userdetails_data = validate_data.pop('userdetails')
        validate_data.pop('password2')
        """
        create_user is a convenience method provided by Django's authentication system. It is typically used to create a new user instance and save it to the database, especially when you're dealing with user authentication. This method takes care of hashing the password before saving it to the database.
        """
        user = User.objects.create_user(**validate_data)
        UserDetails.objects.create(user=user, **userdetails_data)
        return user

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = User
        fields = ['email', 'password']

class UserSerializer(serializers.ModelSerializer):
    allergy = MedicineProblemSerializer(source='medicineproblem_set', many=True, read_only=True)
    created_by = serializers.EmailField(source='created_by.email', read_only=True)
    class Meta:
        model = User
        fields = ['username','email','phone','address','gender','is_active','is_staff','is_admin','allergy','created_by']

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.address = validated_data.get('address', instance.address)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.allergy = validated_data.get('allergy', instance.allergy)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.is_admin = validated_data.get('is_admin', instance.is_admin)
        instance.save()
        return instance


class UserChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={"input_type":"password"}, write_only=True)
    password2 = serializers.CharField(style={"input_type":"password2"}, write_only=True)
    class Meta:
        model = User
        fields = ['password', 'password2']

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        user = self.context.get('user')
        if password != password2:
            raise serializers.ValidationError("Password and confirm password doesn't match")
        user.set_password(password)
        user.save()
        return attrs

class SendPasswordResetEmailSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = User
        fields = ['email']

    def validate(self, attrs):
        email = attrs.get('email')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            print('encoded UID', uid)
            token = PasswordResetTokenGenerator().make_token(user)
            print('password reset token', token)
            link = 'http://localhost:3000/api/user/reset/'+uid+'/'+token
            print('Password Reset Link', link)
            body = 'click Following link to Reset your password ' + link
            data = {
                'email_subject':'Reset Your Password',
                'email_body':body,
                'to_email':user.email
            }
            Util.send_email(data)
            return attrs
        else:
            raise serializers.ValidationError('You are not a registered User')

class UserPasswordResetSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={"input_type":"password"}, write_only=True)
    password2 = serializers.CharField(style={"input_type":"password2"}, write_only=True)
    class Meta:
        model = User
        fields = ['password', 'password2']

    def validate(self, attrs):
        try:
            password = attrs.get('password')
            password2 = attrs.get('password2')
            uid = self.context.get('uid')
            token = self.context.get('token')
            if password != password2:
                raise serializers.ValidationError("Password and confirm password doesn't match")
            id = smart_str(urlsafe_base64_decode(uid))
            user = User.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise serializers.ValidationError("Token is not valid or expired")
            user.set_password(password)
            user.save()
            return attrs
        except DjangoUnicodeDecodeError as identifier:
            PasswordResetTokenGenerator().check_token(user, token)
            raise serializers.ValidationError("Token is not valid or expired")
