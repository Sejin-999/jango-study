from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializer import TestUserSerializer


# Create your views here.

@api_view(['GET'])
def getTestUser(request):
    datas = User.objects.all()
    serializer = TestUserSerializer(datas, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def PostTestUser(request):
    reqData = request.data
    serializer = TestUserSerializer(data=reqData)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data , status=status.HTTP_201_CREATED)
    return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

