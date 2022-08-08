from http import server
import imp
from re import T
from django.shortcuts import redirect, render
from django.urls import reverse
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializer import CreateSuperUserSerializer,LoginUserSerializer
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from serializer import UserDetailSerializer

from authentication import serializer


User=get_user_model()

# Create your views here.

class DummyView(APIView):
    def get(self,request):
        return Response(status=200)


class CreateSuperUserView(APIView):
    def post(self,request):
        data=request.data
        print(data)
        serializer=CreateSuperUserSerializer(data=data)
        if(not serializer.is_valid()):
            return Response(serializer.errors,status=400)

        return Response(status=200)


class LoginUserView(APIView):
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
                print(token[0])
                return Response({'token':token[0].key,'status':200},status=200)

            return Response({'message':'Invalid login credentials'})


class GetUserDetails(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated,IsAdminUser]
    def get(self,request):
        user=request.user
        serializer=UserDetailSerializer(user)
        data=serializer.data
        data['status']=200
        return Response(data=data)