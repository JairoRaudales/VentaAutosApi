from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser

from rest_framework import status

from webapi.models import Modelo
from webapi.serializers import ModeloSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def modelo_list(request):
    if request.method == 'GET':
        modelo = modelo.objects.all()
        modelo_serializer = ModeloSerializer(modelo, many=True)
        return JsonResponse(modelo_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        modelo_data = JSONParser().parse(request)
        modelo_serializer = ModeloSerializer(data=marca_data)
        if modelo_serializer.is_valid():
            modelo_serializer.save()
            return JsonResponse(modelo_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(modelo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def modelo_detail(request, id):
    try:
        modelo = Modelo.objects.get(id=id)
    except Modelo.DoesNotExist:
        return JsonResponse({'message': 'The Modelo does not exist....'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        modelo_serializer = ModeloSerializer(modelo)
        return JsonResponse(modelo_serializer.data)

    elif request.method == 'PUT':
        modelo_data = JSONParser().parse(request)
        modelo_serializer = ModeloSerializer(modelo, data=modelo_data)
        if modelo_serializer.is_valid():
            modelo_serializer.save()
            return JsonResponse(modelo_serializer.data)
        return JsonResponse(modelo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        modelo.delete()
        return JsonResponse({'message': 'Modelo was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)