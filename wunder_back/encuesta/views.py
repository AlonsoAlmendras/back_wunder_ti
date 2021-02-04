from django.shortcuts import render, redirect  
from encuesta.serializers import EncuestaSerializer
from encuesta.models import Encuesta 

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from django.http import HttpResponse, response
from django.http import JsonResponse
from django.core import serializers

import json
from django.core.exceptions import ObjectDoesNotExist

@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])  
def welcome(request):
    content = {"message": "Bienvenido a las encuestas!"}
    return JsonResponse(content)

@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_encuesta(request):
    user = request.user.id
    encuestas = Encuesta.objects.all()
    serializer = EncuestaSerializer(encuestas, many=True)
    return JsonResponse({'encuestas': serializer.data}, safe=False, status=status.HTTP_200_OK)

@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add_encuesta(request):
    payload = json.loads(request.body)
    user = request.user
    try:
        encuesta = Encuesta.objects.create(
            nombre_encuesta=payload["nombre_encuesta"],
            texto_encuesta=payload["descripcion_encuesta"],
            puntaje_total=payload["puntaje_total_encuesta"],
        )
        serializer = EncuestaSerializer(encuesta)
        return JsonResponse({'encuesta': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Paso algo terrible!'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["PUT"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def update_encuesta(request, encuesta_id):
    user = request.user.id
    payload = json.loads(request.body)
    try:
        encuesta_item = Encuesta.objects.filter(id=encuesta_id)
        # returns 1 or 0
        encuesta_item.update(**payload)
        encuesta = Encuesta.objects.get(id=encuesta_id)
        serializer = EncuestaSerializer(encuesta)
        return JsonResponse({'encuesta': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Paso algo terrible!'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_encuesta(request, encuesta_id):
    user = request.user.id
    try:
        encuesta = Encuesta.objects.get(id=encuesta_id)
        encuesta.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)