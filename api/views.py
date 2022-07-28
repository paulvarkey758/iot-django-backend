from django.shortcuts import render
from .models import Component
from .serializers import ComponentSerializer
from rest_framework.decorators import api_view,parser_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
import json

# Create your views here.
@api_view(['GET'])
def readData(request):
    d=Component.objects.all()
    print(d)
    serializer=ComponentSerializer(d, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
@parser_classes([JSONParser])
def writeData(request,pk):
    d=Component.objects.get(id=pk)
    serializer=ComponentSerializer(instance=d,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)   

@api_view(['POST'])
@parser_classes([JSONParser])
def createData(request):
    data=json.loads(request.data)
    serializer=ComponentSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response("serializer is not valid")                  