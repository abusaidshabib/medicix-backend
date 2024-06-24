from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status

# My created
from .serializers import MedicineSerializer
from authentication.permissions import IsAdmin
from .models import Medicine

# Create your views here.
class MedicineInventoryCreateView(APIView):
    permission_classes = [IsAdmin]

    def post(self, request):
        serializer = MedicineSerializer(data=request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response({'branch': "MedicineSerializer", 'success': True}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
