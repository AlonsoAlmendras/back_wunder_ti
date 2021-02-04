from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .serializers import PreguntaSerializer
from .models import Pregunta
from rest_framework import status

from .models import Pregunta
import json
from django.core.exceptions import ObjectDoesNotExist


@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])  
def welcome(request):
    content = {"message": "Bienvenido a las preguntas!"}
    return JsonResponse(content)

#User can get all preguntas
@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_preguntas(request):
    user = request.user.id
    preguntas = Pregunta.objects.filter(added_by=user)
    serializer = PreguntaSerializer(preguntas, many=True)
    return JsonResponse({'preguntas': serializer.data}, safe=False, status=status.HTTP_200_OK)


# User can add a Preguntas
#@api_view(["POST"])
#@csrf_exempt
#@permission_classes([IsAuthenticated])
#def add_preguntas(request):
#    payload = json.loads(request.body)
#    user = request.user
#    try:
#        pregunta = Pregunta.objects.create(
#            texto_pregunta = payload["Pregunta"],
#            tipo_pregunta = payload["Tipo de pregunta"],
#            alternativa = payload["Respuestas o alternativas"],
#            estado = payload["Estado de la pregunta"],
#            pub_date = payload["Fecha de la pregunta"], 
#        )
#        serializer = PreguntaSerializer(pregunta)
#        return JsonResponse({'preguntas': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
#    except ObjectDoesNotExist as e:
#        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
#    except Exception:
#        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)