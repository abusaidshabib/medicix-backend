from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import MyUser
from .serializers import MyUserSerializer

# Create your views here.
class UsersView(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    def get(self, request):
        users = MyUser.objects.all()
        serializer = MyUserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)