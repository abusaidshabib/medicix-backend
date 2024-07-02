from rest_framework import serializers

from .models import Medicine, Inventory
from authentication.models import User

"""
class Inventory(BaseModel):
    medicine = models.ForeignKey(Medicine, verbose_name=_("Medicine"), on_delete=models.CASCADE, related_name='')
    branch = models.ForeignKey(Branch, verbose_name=_("Branch"), on_delete=models.CASCADE, related_name='')
    quantity = models.IntegerField()

    class Meta:
        unique_together = ["medicine", "branch"]

    def __str__(self):
        return f"{self.medicine} at {self.branch}"

    def clean(self):
        if self.soled > self.quantity:
            raise ValidationError(_("The sold quantity cannot exceed the available quantity."))
"""

class InventorySerializer(serializers.ModelSerializer):
    branch_name = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Inventory
        fields = ["medicine","branch_name","quantity"]
        extra_kwargs = {
            'medicine': {'write_only': True},
        }

    def get_branch_name(self, obj):
        return obj.branch.name if obj.branch else None

    # def create(self, validated_data):

class MedicineSerializer(serializers.ModelSerializer):
    inventories_medicine = serializers.SerializerMethodField()
    # inventories_medicine = InventorySerializer(many=True, read_only=True)
    class Meta:
        model = Medicine
        fields = ["brand", "manufacturer", "generic","strength", "price", "use_for", "dar", "inventories_medicine"]

    def get_inventories_medicine(self, obj):
        branch = self.context.get('branch')
        if branch:
            inventories = obj.inventories.filter(branch=branch)
        else:
            inventories = obj.inventories.all()
        return InventorySerializer(inventories, many=True).data

    # def create(self, validated_data):


    # def create(self, validated_data):
    #     user = self.context['request'].user
    #     medicine_quantity = validated_data.pop('quantity')
    #     branch = user.branch

    #     try:
    #         medicines = Medicine.objects.get_or_create(**validated_data)
    #     except Medicine.DoesNotExist:
    #         return serializers.ValidationError("The medicine is created multiple please check it")

    #     print(medicines)

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