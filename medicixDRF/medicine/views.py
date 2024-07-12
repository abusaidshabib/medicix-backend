from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status

# My created
from .serializers import MedicineSerializer
from authentication.permissions import IsAdmin
from .models import Medicine, Inventory

# Create your views here.
# class MedicineInventoryCreateView(APIView):
#     permission_classes = [IsAdmin]

#     def post(self, request):
#         serializer = MedicineSerializer(data=request.data, context={'request':request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'branch': "MedicineSerializer", 'success': True}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MedicineGetView(APIView):
    # permission_classes = [AllowAny]

    def get(self, request):
        branch = request.user.branch if not request.user.is_superuser else None
        if request.user.is_superuser:
            medicines = Medicine.objects.all()
        elif request.user.is_admin or request.user.is_staff:
            inventories = Inventory.objects.filter(branch=branch)
            medicine_ids = inventories.values_list('medicine_id', flat=True)
            medicines = Medicine.objects.filter(id__in=medicine_ids)
        else:
            medicines = Medicine.objects.none()
        serializer = MedicineSerializer(medicines, many=True, context={'branch': branch})
        return Response(serializer.data, status=status.HTTP_200_OK)

    # def post(self, request, format=None):
    #     serializer =
            # inventories = Inventory.objects.filter(branch=branch)