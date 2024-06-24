from rest_framework import serializers
from .models import Branch, BranchAddress

class BranchAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchAddress
        fields = ["house_number", "holding_number", "street_name", "village", "post_office", "district", "city", "state", "post_code", "country"]

class BranchSerializer(serializers.ModelSerializer):
    branchaddress = BranchAddressSerializer(required=True)

    class Meta:
        model = Branch
        fields = ["name", "branchaddress"]
        read_only_fields = ['branch_code', 'created_by']

    def create(self, validated_data):
        branchaddress_data = validated_data.pop('branchaddress')
        last_branch = Branch.objects.last()
        if not last_branch:
            branch_code = 'BR1'
        else:
            branch_code = f'BR{last_branch.id + 1}'
        validated_data['branch_code'] = branch_code
        validated_data['created_by'] = self.context['request'].user

        branch = Branch.objects.create(**validated_data)
        BranchAddress.objects.create(branch=branch, **branchaddress_data)

        return branch

    def update(self,instance ,validated_data):
        branchaddress_data = validated_data.pop('branchaddress')
        branchaddress_instance = instance.branchaddress
        
        instance.name = validated_data.get('name', instance.name)
        instance.save()

        branchaddress_instance.house_number = branchaddress_data.get('house_number', branchaddress_instance.house_number)
        branchaddress_instance.holding_number = branchaddress_data.get('holding_number', branchaddress_instance.holding_number)
        branchaddress_instance.street_name = branchaddress_data.get('street_name', branchaddress_instance.street_name)
        branchaddress_instance.village = branchaddress_data.get('village', branchaddress_instance.village)
        branchaddress_instance.post_office = branchaddress_data.get('post_office', branchaddress_instance.post_office)
        branchaddress_instance.district = branchaddress_data.get('district', branchaddress_instance.district)
        branchaddress_instance.city = branchaddress_data.get('city', branchaddress_instance.city)
        branchaddress_instance.state = branchaddress_data.get('state', branchaddress_instance.state)
        branchaddress_instance.post_code = branchaddress_data.get('post_code', branchaddress_instance.post_code)
        branchaddress_instance.country = branchaddress_data.get('country', branchaddress_instance.country)
        branchaddress_instance.save()

        return instance