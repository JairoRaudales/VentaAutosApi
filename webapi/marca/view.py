from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser

from rest_framework import status

from webapi.models import Marca
from webapi.serializers import MarcaSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def marca_list(request):
    if request.method == 'GET':
        marca = marca.objects.all()
        marca_serializer = MarcaSerializer(marca, many=True)
        return JsonResponse(marca_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        marca_data = JSONParser().parse(request)
        marca_serializer = MarcaSerializer(data=marca_data)
        if marca_serializer.is_valid():
            marca_serializer.save()
            return JsonResponse(marca_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(marca_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def marca_detail(request, id):
    try:
        marca = Marca.objects.get(id=id)
    except Marca.DoesNotExist:
        return JsonResponse({'message': 'The Marca does not exist....'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        marca_serializer = MarcaSerializer(marca)
        return JsonResponse(marca_serializer.data)

    elif request.method == 'PUT':
        marca_data = JSONParser().parse(request)
        marca_serializer = MarcaSerializer(marca, data=marca_data)
        if marca_serializer.is_valid():
            marca_serializer.save()
            return JsonResponse(marca_serializer.data)
        return JsonResponse(marca_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        marca.delete()
        return JsonResponse({'message': 'Marca was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)