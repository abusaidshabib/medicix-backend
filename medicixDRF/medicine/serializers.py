from rest_framework import serializers

from .models import Medicine, Inventory
from authentication.models import User

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ["medicine","branch","quantity"]
class MedicineSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField()
    class Meta:
        model = Medicine
        fields = ["quantity","brand", "manufacturer", "generic","strength", "price", "use_for", "dar", "total", "expire_date","subcategory_id"]

    def create(self, validated_data):
        user = self.context['request'].user
        medicine_quantity = validated_data.pop('quantity')
        branch = user.branch

        try:
            medicines = Medicine.objects.get_or_create(**validated_data)
        except Medicine.DoesNotExist:
            return serializers.ValidationError("The medicine is created multiple please check it")

        print(medicines)

    # def create(self, validated_data):
    #     branchaddress_data = validated_data.pop('branchaddress')
    #     last_branch = Branch.objects.last()
    #     if not last_branch:
    #         branch_code = 'BR1'
    #     else:
    #         branch_code = f'BR{last_branch.id + 1}'
    #     validated_data['branch_code'] = branch_code
    #     validated_data['created_by'] = self.context['request'].user

    #     branch = Branch.objects.create(**validated_data)
    #     BranchAddress.objects.create(branch=branch, **branchaddress_data)

    #     return branch

        # medicine = attrs.get('medicine')

    # def create(self, validate_data):
    #     inventory_data = validate_data.pop('inventory')
    #     medicine = Medicine.objects.create(**validate_data)
    #     inventory_data