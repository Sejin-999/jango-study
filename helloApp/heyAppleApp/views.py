import pymysql
from django.http import JsonResponse
import boto3
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Fruit
from .serializers import FruitSerializer
# Create your views here.

#db = pymysql.Connect(host="localhost" , user="root" , password="1234" , database="heyAppledb")
#cursor = db.cursor();

# 전체 정보 넘겨주는 함수 ... 삭제되거나 , 값이 없는 경우 에외처리
@api_view(['GET'])
def getFruitInfo(request):
    datas = Fruit.objects.filter(is_deleted =1).all()
    if datas is not None:  # datas != none
        serializer = FruitSerializer(datas , many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)
    return JsonResponse({"msg":"Infomation not found"} , status=status.HTTP_401_UNAUTHORIZED)


# 찾고 싶은 과일 정보 찾기 (세부페이지)
@api_view(['POST'])
def postFruitFind(request):
    reqData = request.data
    name = reqData['name']  #id or name 
    data = Fruit.objects.filter(name = name)
    if data is not None:  # datas != none
        serializer = FruitSerializer(data,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return JsonResponse({"msg":"Infomation not found"} , status=status.HTTP_401_UNAUTHORIZED)





