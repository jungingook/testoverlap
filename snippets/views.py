from django.shortcuts import render #?
from .models import * # 모델

from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response  #응답 모듈
from .serializer import *
from django.http import JsonResponse #제이슨용 응답 모듈
# Create your views here.


@csrf_exempt
def test(request,userid) :
    ############################################
    # GET 으로 받는 경우
    ############################################
    if request.method == "GET" : 
        user = User.objects.get(userID=userid)
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)
