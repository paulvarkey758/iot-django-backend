from django.shortcuts import render
from .models import Component
from .serializers import ComponentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def readData(request):
    d=Component.objects.all()
    serializer=ComponentSerializer(d, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def writeData(request,pk):
    d=Component.objects.get(id=pk)
    serializer=ComponentSerializer(instance=d,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data) 
    else:
        return Response("serializer is not valid")         

@api_view(['POST'])
def createData(request):
    serializer=ComponentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response("serializer is not valid")                  