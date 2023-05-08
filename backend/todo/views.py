from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework import viewsets
from rest_framework import permissions
from .models import Todo, Group
from .serializers import TodoSerializer, GroupTodosSerializer, GroupSerializer
from datetime import datetime

import json

class TodoView(APIView):
    queryset = Todo.objects.all()

    def put(self, request, *args, **kwargs):
        ''' This function handles drag n drop'''
        todo_list = request.data
        instances = []
        for todo in todo_list:
            obj = self.queryset.get(id=todo["id"])
            obj.pos = todo["pos"]
            obj.groupId = Group.objects.get(id=todo["groupId"])
            obj.save()
            instances.append(obj)
        
        serializer = TodoSerializer(instances, many=True)
        return Response(serializer.data)
    
    def get(self, request):
        serializer = TodoSerializer(self.queryset.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        ''' This function creates a new todo'''
        entry = Todo(title=request.data['title'], description=request.data['description'], groupId = Group.objects.get(id =request.data['groupId']), pos=9999, deadline = request.data['deadline'])
        entry.save()

        serializer = TodoSerializer(entry)
        return Response(serializer.data)
    
class GroupTodoView(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupTodosSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.order_by('id')

    def perform_create(self, serializer):
        return serializer.save();    

class GroupView(viewsets.ModelViewSet): 
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def get_queryset(self):
        return self.queryset.order_by('id')
    
    def perform_create(self, serializer):
        return serializer.save()