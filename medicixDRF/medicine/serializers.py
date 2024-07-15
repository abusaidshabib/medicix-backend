from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Medicine, Inventory
from content.serializers import SubcategorySerializer
from content.models import Subcategory



class InventorySerializer(serializers.ModelSerializer):
    medicine = serializers.SlugRelatedField(slug_field='brand', queryset=Medicine.objects.all(), write_only=True)

    class Meta:
        model = Inventory
        fields = ['medicine', 'quantity', 'expire_date', 'soled']
        extra_kwargs = {
            'soled': {'read_only': True}
        }

    def validate(self, data):
        request = self.context.get('request')
        branch = request.user.branch
        medicine = data['medicine']
        if not branch:
            raise ValidationError({'field_errors':'user is not assign in branch'})
        if Inventory.objects.filter(medicine=medicine, branch=branch).exists():
            raise ValidationError({'non_field_errors': 'This medicine already exists in this branch inventory.'})

        return data

    def create(self, validated_data):
        request = self.context.get('request', None)
        user = request.user
        branch = user.branch
        inventory = Inventory.objects.create(branch=branch, **validated_data)
        return inventory

    # def update(self, instance, validated_data):
    #     instance.e

class MedicineSerializer(serializers.ModelSerializer):
    subcategory = serializers.SlugRelatedField(slug_field='name', queryset=Subcategory.objects.all(), write_only=True)
    inventories = InventorySerializer(many=True, read_only=True)
    class Meta:
        model = Medicine
        fields = ['brand', 'manufacturer', 'generic', 'strength', 'subcategory', 'price', 'medicine_type', 'use_for', 'dar','inventories']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get('request', None)
        user = request.user
        branch = user.branch
        if branch:
            inventories = instance.inventories.filter(branch__name=branch)
        else:
            inventories = instance.inventories.all()
        representation['inventories'] = InventorySerializer(inventories, many=True).data
        return representation



"""
from rest_framework import serializers
from .models import Inventory, Medicine

class InventorySerializer(serializers.ModelSerializer):
    medicine = serializers.SlugRelatedField(slug_field='brand', queryset=Medicine.objects.all())

    class Meta:
        model = Inventory
        fields = ['medicine', 'quantity', 'expire_date']

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        branch = user.branch  # Adjust based on how branch is related to the user

        inventory = Inventory.objects.create(branch=branch, **validated_data)
        return inventory

    def update(self, instance, validated_data):
        request = self.context.get('request')
        user = request.user
        branch = user.branch  # Adjust based on how branch is related to the user

        instance.medicine = validated_data.get('medicine', instance.medicine)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.expire_date = validated_data.get('expire_date', instance.expire_date)
        instance.branch = branch
        instance.save()
        return instance
"""