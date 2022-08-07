from http import server
import imp
from django.shortcuts import redirect, render
from django.urls import reverse
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializer import CreateSuperUserSerializer,LoginUserSerializer
from django.contrib.auth import authenticate


User=get_user_model()

# Create your views here.
class CreateSuperUser(APIView):
    def post(self,request):
        data=request.data
        print(data)
        serializer=CreateSuperUserSerializer(data=data)
        if(not serializer.is_valid()):
            return Response(serializer.errors,status=400)

        return Response(status=200)


class LoginUser(APIView):
    def post(self,request):
        data=request.data
        serializer=LoginUserSerializer(data=data)
        if(not serializer.is_valid()):
            return Response(serializer.errors,status=400)
        else:
            user=authenticate(username=data['username'],
            password=data['password'])

            if user:
                token=Token.objects.get_or_create(user=user)
                return Response({'token':token.key})

            return Response({'message':'Invalid login credentials'})


