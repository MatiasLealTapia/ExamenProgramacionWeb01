from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view # sin este no puedo crear la api
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token

@api_view(['POST'])
def login_user(request):
    data=JSONParser().parse(request)
    username=data['username']
    password=data['password']
    try:
        user=User.objects.get(username=username)
    except User.DoesNotExist:
        return Response("Usuario no existe")
    #validar password contraseña
    pass_valido = check_password(password, user.password)
    if not pass_valido:
        return Response("Contraseña incorrecta")
    #crear token
    token, created = Token.objects.get_or_create(user=user)
    return Response(token.key)