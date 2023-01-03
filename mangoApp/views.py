from django.shortcuts import render,redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import user
from .serializers import TestUserSerializer
# Create your views here.
''' 
    나중에 리엑트랑 연동시키기위해서 json 형식으로 주기 위해 세팅해보기
    api_view part
'''
# all User .. Start
@api_view(['GET'])
def jsonGetAllUser(request):
    datas = user.objects.all()
    serializer = TestUserSerializer(datas , many=True)
    return Response(serializer.data)
# all User ..  End


'''
    템플릿 엔진으로 실제로 잘 구동되는지 확인해보기
'''

def TempGetAllUser(request):
    datas = user.objects.all()
    return render(request , 'getAlluser.html', {'datas':datas})