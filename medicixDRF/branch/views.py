from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status

# my created
from .serializers import BranchSerializer
from authentication.permissions import IsAdmin
from .models import Branch
# Create your views here.

class BranchesCreateView(APIView):
    permission_classes = [IsAdmin]

    def get(self, request):
        branches = Branch.objects.all()
        serializers = BranchSerializer(branches, many=True)
        return Response({'branches': serializers.data, 'success': True}, status=status.HTTP_201_CREATED)

    def post(self, request, format=None):
        serializer = BranchSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            branch = serializer.save()
            branch_data = BranchSerializer(branch).data
            return Response({'branch': branch_data, 'success': True}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BranchGetUpdateView(APIView):
    def get(self, request, key):
        branches = Branch.objects.get(branch_code=key)
        serializers = BranchSerializer(branches)
        return Response({'branches': serializers.data, 'success': True}, status=status.HTTP_201_CREATED)

    def put(self, request, key):
        try:
            branch = Branch.objects.get(branch_code=key)
        except Branch.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = BranchSerializer(branch, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, key):
        try:
            branch = Branch.objects.get(branch_code=key)
        except Branch.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        branch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
