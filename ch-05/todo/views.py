from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from .serializers import TodoSimpleSerializer, TodoDetailSerializer, TodoCreateSerializer
from .models import Todo
import sys

FUNC_NAME = "sys._getframe().f_code.co_name"

class HelloAPIView(APIView):
    def get(self, request, *args, **kwargs):
        print("%s/%s: get" % (self.__class__.__name__, sys._getframe().f_code.co_name))
        return Response("Hello World")


# Create your views here.
class TodosAPIView(APIView):
    def get(self, request):
        print("%s: get" % self.__class__.__name__)
        todos = Todo.objects.filter(complete=False)
        serial = TodoSimpleSerializer(todos, many=True)
        return Response(serial.data, status=status.HTTP_200_OK) # Response타입의객체생성해서 리턴.

    def post(self, request):
        print("%s: post" % self.__class__.__name__)
        serial = TodoCreateSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status = status.HTTP_201_CREATED)

        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoAPIView(APIView):
    def get(self, request, id):
        print("%s: get, id %d" % (self.__class__.__name__, id))
        todo = get_object_or_404(Todo, id=id)
        serial = TodoDetailSerializer(todo)
        return Response(serial.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        print("%s/%s: get, id %d" % (self.__class__.__name__, eval(FUNC_NAME), id))
        todo = get_object_or_404(Todo, id = id)
        serial = TodoCreateSerializer(todo, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_200_OK)

        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)


class DoneTodosAPIView(APIView):
    def get(self, request):
        print("%s: get" % (self.__class__.__name__))
        todos = Todo.objects.filter(complete=True)
        serial = TodoSimpleSerializer(todos, many=True)
        return Response(serial.data, status=status.HTTP_200_OK)

class DoneTodoAPIView(APIView):
    def get(self, request, id):
        print("%s: get" % (self.__class__.__name__))
        todo = get_object_or_404(Todo, id = id)
        todo.complete = True
        todo.save()
        serial = TodoDetailSerializer(todo)
        return Response(serial.data, status=status.HTTP_200_OK)

