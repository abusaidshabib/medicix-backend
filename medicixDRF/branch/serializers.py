from rest_framework import serializers
from .models import Branch, BranchAddress

class BranchAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchAddress
        fields = ["house_number", "holding_number", "street_name","village","post_office","district", "city", "state", "post_code","country"]
        extra_kwargs = {
            "house_number":{"required":False},
            "holding_number":{"required":False},
            "street_name":{"required":False},
            "village":{"required":False},
            "post_office":{"required":False},
            "district":{"required":False},
            "city":{"required":False},
            "state":{"required":False},
            "post_code":{"required":False},
            "country":{"required":False}
        }

class BranchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Branch
        fields = ["name"]

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        branch = Branch.objects.create(**validated_data)
        BranchAddress.objects.create(branch=branch, **address_data)
        return branch

    # def update(self, instance, validated_data):
    #     address_data = validated_data.pop('address')
    #     address_instance = instance.address
