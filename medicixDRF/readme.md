# models.py
from django.db import models
from branch.models import BaseModel, Branch
from django.utils.translation import gettext as _

class Medicine(BaseModel):
    brand = models.CharField(max_length=200, unique=True)
    manufacturer = models.CharField(max_length=255)
    generic = models.CharField(max_length=150)
    strength = models.CharField(max_length=150)
    subcategory = models.ForeignKey("content.Subcategory", on_delete=models.CASCADE, related_name='medicines')
    price = models.FloatField()

    MEDICINE_CATEGORY = [
        #... (categories list)
    ]

    MEDICINE_FOR = [
        ("H","Human"),
        ("V","Veterinary"),
        ("R","R"),
    ]
    medicine_type = models.CharField(max_length=50, choices=MEDICINE_CATEGORY)
    use_for = models.CharField(max_length=50, choices=MEDICINE_FOR)
    dar = models.CharField(max_length=200)

    def __str__(self):
        return self.generic

class Inventory(BaseModel):
    medicine = models.ForeignKey(Medicine, verbose_name=_("Medicine"), on_delete=models.CASCADE, related_name='inventories')
    branch = models.ForeignKey(Branch, verbose_name=_("Branch"), on_delete=models.CASCADE)
    quantity = models.IntegerField()
    soled = models.IntegerField(blank=True, null=True)
    expire_date = models.DateField()

    class Meta:
        unique_together = ["medicine", "branch"]

    def __str__(self):
        return f"{self.medicine} at {self.branch}"

    def clean(self):
        if self.soled > self.quantity:
            raise ValidationError(_("The sold quantity cannot exceed the available quantity."))

# serializers.py
from rest_framework import serializers
from .models import Inventory, Medicine

class InventorySerializer(serializers.ModelSerializer):
    medicine = serializers.SlugRelatedField(slug_field='brand', queryset=Medicine.objects.all())

    class Meta:
        model = Inventory
        fields = ['medicine', 'quantity', 'expire_date']

    def validate(self, data):
        request = self.context.get('request')
        branch = request.user.branch
        medicine = data['medicine']

        if Inventory.objects.filter(medicine=medicine, branch=branch).exists():
            raise serializers.ValidationError({'non_field_errors': 'This medicine already exists in this branch inventory.'})

        return data

    def create(self, validated_data):
        request = self.context.get('request')
        branch = request.user.branch
        inventory = Inventory.objects.create(branch=branch, **validated_data)
        return inventory

class MedicineSerializer(serializers.ModelSerializer):
    subcategory = serializers.SlugRelatedField(slug_field='name', queryset=Subcategory.objects.all())

    class Meta:
        model = Medicine
        fields = ['brand', 'manufacturer', 'generic', 'strength', 'subcategory', 'price', 'medicine_type', 'use_for', 'dar']


# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Medicine, Inventory
from .serializers import InventorySerializer

class AddInventoryForAllMedicines(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        branch = request.user.branch
        medicines = Medicine.objects.all()
        created_inventories = []

        for medicine in medicines:
            inventory_data = {
                'medicine': medicine,
                'branch': branch,
                'quantity': 0,  # default quantity
                'expire_date': None  # default expire date, you might want to update this
            }
            serializer = InventorySerializer(data=inventory_data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                created_inventories.append(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(created_inventories, status=status.HTTP_201_CREATED)


# urls.py
from django.urls import path
from .views import AddInventoryForAllMedicines

urlpatterns = [
    path('inventory/add-for-all/', AddInventoryForAllMedicines.as_view(), name='inventory-add-for-all'),
]
