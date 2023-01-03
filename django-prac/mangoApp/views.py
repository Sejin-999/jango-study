from django.shortcuts import render,redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Usertable
from .serializers import TestUserSerializer
# Create your views here.
''' 
    나중에 리엑트랑 연동시키기위해서 json 형식으로 주기 위해 세팅해보기
    api_view part
'''
# all User .. Start
@api_view(['GET'])
def jsonGetAllUser(request):
    datas = Usertable.objects.all()
    serializer = TestUserSerializer(datas , many=True)
    return Response(serializer.data)
# all User ..  End


# post user data .. start
@api_view(['POST'])
def jsonPostUser(request):
    if request.method=="POST":
        reqData = request.data
        serializer = TestUserSerializer(data=reqData)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data , status=status.HTTP_201_CREATED)
    return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST) 
# post user data .. End

'''
    템플릿 엔진으로 실제로 잘 구동되는지 확인해보기
'''

#all User .. Start
def TempGetAllUser(request):
    datas = Usertable.objects.all()
    return render(request , 'getAlluser.html', {'datas':datas})
#all User .. End 

# post user data .. start
def TempPostUser(request):
    if request.method=="POST":
        datas = Usertable()
        Usertable.userId = request.POST['userId']
        Usertable.userPass= request.POST['userPass']
        return redirect('/mangoApp/tempGetAllUser/')
    else :
        datas = Usertable()
        return render(request , 'postUser.html', {'datas':datas})
# post user data .. End


#http://localhost:8000/mangoApp/TempPostUser
