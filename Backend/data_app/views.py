from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework import viewsets
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpRequest
from rest_framework.permissions import IsAuthenticated, AllowAny
import json
class UserDetailsView(APIView):
  permission_classes = (AllowAny,)
  def post(self,request):
    serializer = UserDetailsSerializer(data=request.data)

    if not serializer.is_valid():
      print(serializer.errors)
      return Response({'status':200,'errors':serializer.errors})
    serializer.save()
    return Response({'status':200,'payload':serializer.data})

  # def login(self,request):
  #   dd = LoginDataSerializer(request.data)
  #   abcd = UserDetails.objects.filter(email=dd.get('email')).values()
  #   serializer = UserDetailsSerializer(abcd,many=True)
  #   return Response({'status':200,'payload':serializer.data})


class ManageBinsView(APIView):
  permission_classes = (AllowAny,)
  def post(self,request):
    serializer = ManageBinsSerializer(data=request.data)
    if not serializer.is_valid():
      print(serializer.errors)
      return Response({'status':200,'errors':serializer.errors})
    serializer.save()
    return Response({'status':200,'payload':serializer.data})
  
  # def DELETE(self,request,id):
  #   data = ManageBins.objects.filter(id=id).delete()
  #   temp_data = ManageBins.objects.all()
  #   ss = ManageBinsSerializer(data=temp_data)
  #   return Response({'status':200,'data':ss.data})

class WorkerDetailsView(APIView):
  permission_classes = (AllowAny,)
  def post(self,request):
    serializer = WorkerDetailsSerializer(data=request.data)
    if not serializer.is_valid():
      print(serializer.errors)
      return Response({'status':200,'errors':serializer.errors})
    serializer.save()
    return Response({'status':200,'payload':serializer.data})

class TrackTruckView(APIView):
  permission_classes = (AllowAny,)
  def post(self,request):
    serializer = TrackTruckSerializer(data=request.data)
    if not serializer.is_valid():
      print(serializer.errors)
      return Response({'status':200,'errors':serializer.errors})
    serializer.save()
    return Response({'status':200,'payload':serializer.data})

class TrackWorkerView(APIView):
  permission_classes = (AllowAny,)
  def post(self,request):
    serializer = TrackWorkerSerializer()(data=request.data)
    if not serializer.is_valid():
      print(serializer.errors)
      return Response({'status':200,'errors':serializer.errors})
    serializer.save()
    return Response({'status':200,'payload':serializer.data})

class complaintView(APIView):
  permission_classes = (AllowAny,)
  def post(self,request):
    serializer = ComplaintSerializer(data=request.data)
    if not serializer.is_valid():
      print(serializer.errors)
      return Response({'status':200,'errors':serializer.errors})
    serializer.save()
    return Response({'status':200,'payload':serializer.data})

  def get(self,request):
    obj = complaints.objects.get('address','complaint','tags')
    serializer = ComplaintSerializer(data=obj)
    return Response(data=serializer.data)

class ManageHouseView(APIView):
  permission_classes = (AllowAny,)
  def post(self,request):
    serializer = ManageBinsSerializer(data=request.data)
    if not serializer.is_valid():
      print(serializer.errors)
      return Response({'status':200,'errors':serializer.errors})
    serializer.save()
    return Response({'status':200,'payload':serializer.data})

class pickupView(APIView):
  permission_classes = (AllowAny,)
  def post(self,request):
    serializer = pickupSerializer(data=request.data)
    if not serializer.is_valid():
      print(serializer.errors)
      return Response({'status':200,'errors':serializer.errors})
    serializer.save()
    return Response({'status':200,'payload':serializer.data})
  
  def get(self,request):
    obj = pickup.objects.all()
    serializer = pickupSerializer(data=obj)
    return Response(data=serializer.data)