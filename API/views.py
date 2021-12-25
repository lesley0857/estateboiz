from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView
import json
from rest_framework.permissions import AllowAny,IsAuthenticatedOrReadOnly,IsAuthenticated
from rest_framework.views import View,APIView
from England.models import Groupss,Chatmessage
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST
from .serializer import *

# Create your views here.

class list_api(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Groupss.objects.all()
    serializer_class = Group_serializer

@api_view(['GET'])
def chatmessage_retrieve_api(request,id):
    g = Groupss.objects.get(id=id)
    chatt = Chatmessage.objects.filter(id=g.id)
    print('chatt',chatt)
    queryset = Groupss.objects.all()
    serializer = Chatmessage_serializer(chatt,many=True)
    #queryset = Groupss.objects.all()
    return Response(serializer.data, status=HTTP_200_OK)

@api_view(['POST'])
def user_creation_api(request):
    print('valid',request.data)
    serializer = user_creation_serializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        print('serializer is valid')
        serializer.save()
        return Response(serializer.data, status=HTTP_200_OK)
    return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)


class chatmessage_create_api(APIView):
    permission_classes = [AllowAny]
    def post(self,request,*args,**kwargs):
        data = request.data
        print(data)
        serializer =  Group_serializer
        return Response (data,status=HTTP_200_OK)

class user_login_api(APIView):
    #permission_classes = [IsAuthenticated]
    def post(self,request,*args,**kwargs):
        data = request.data
        print(data)
        serializer =  user_login_serializer(data=data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.data
            return Response (data,status=HTTP_200_OK)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)