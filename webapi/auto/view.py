from django.shortcuts import render
from django.shortcuts import get_object_or_404

# Create your views here.
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from webapi.models import Auto, AutoColor, Color, Estado
from webapi.serializers import AutoSerializer, AutoColorSerializer, ColorSerializer, EstadoSerializer

from rest_framework.decorators import api_view
from django.db.utils import IntegrityError

from django.db.models import Count


from pymongo import MongoClient

from webapi.dbclasses.cliente import ClienteCollection
from django.db.models import Case, When, Value, IntegerField

import pandas as pd

# Create your views here.
@api_view(['POST'])
def auto_list(request):
    if request.method == 'POST':
        auto_data = JSONParser().parse(request)
        auto_serializer = AutoSerializer(data=auto_data)
        if auto_serializer.is_valid():
            auto_serializer.save()
            return JsonResponse(auto_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(auto_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def auto_detail(request, id):
    auto = get_object_or_404(Auto, id=id)
    if request.method == 'GET':
        auto_serializer = AutoSerializer(auto)
        return JsonResponse(auto_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'PUT':
        auto_data = JSONParser().parse(request)
        auto_data["id"] = id
        auto_serializer = AutoSerializer(auto, data=auto_data)
        if auto_serializer.is_valid():
            auto_serializer.save()
            return JsonResponse(auto_serializer.data)
        return JsonResponse(auto_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        auto.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def auto_colores(request, id):
    auto = get_object_or_404(Auto, id=id)
    if request.method == 'GET':
        colores = AutoColor.objects.filter(id_auto=auto)
        colores_serializer = AutoColorSerializer(colores, many=True)
        return JsonResponse(colores_serializer.data, safe=False)
    
    elif request.method == 'POST':
        colores_data = JSONParser().parse(request)
        colores_data["id_auto"] = id
        colores_serializer = AutoColorSerializer(data=colores_data)
        if colores_serializer.is_valid():
            colores_serializer.save()
            return JsonResponse(colores_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(colores_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def auto_colores_detail(request, id, id_color):
    if request.method == 'DELETE':
        auto = get_object_or_404(Auto, id=id)
        color = get_object_or_404(Color, id=id_color)
        auto_color = get_object_or_404(AutoColor, id_color=color, id_auto=auto)        
        auto_color.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

    
@api_view(['DELETE'])
def auto_estado_detail(request, id, id_estado):
    if request.method == 'DELETE':
        auto = get_object_or_404(Auto, id=id)
        estado = get_object_or_404(Estado, id=id_estado)
        auto_estado = get_object_or_404(Estado, id_estado=estado, id_auto=auto)        
        auto_estado.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)