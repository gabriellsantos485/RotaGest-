"""
Usuario do sistema - Garçon ou Admin

Arquivo respnsável pela lógica da api de devolver e setar dados 
dos usuarios 
Gabriel Rodrigues dos Santos
28/03/2025
"""
from restaurante.models import Usuario
from restaurante.serializers import UsuarioSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework import status
from restaurante.serializers import LoginSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import AllowAny

class AutenticacaoServices(ViewSet):
    """ ViewSet para autenticação de usuários """

    queryset = Usuario.objects.all()
    serializer_class =UsuarioSerializer
    permission_classes = [AllowAny]
    
    @action(detail=False, methods=['post'], url_name="criar-login")
    def create_user(self, request):
        """
        Cria um novo usuário.

        Este método lida com a criação de novos usuários, utilizando o
        UserSerializer para validar e salvar os dados.
        """
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['post'], url_name="login")
    def login(self, request):
        """
        Realiza o login de um usuário.

        Este método lida com o login de usuários existentes, validando
        as credenciais e retornando um token de autenticação.
        """
        serializer = LoginSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response(serializer.data,  status=status.HTTP_200_OK)
        return Response(data=serializer.data, status=status.HTTP_401_UNAUTHORIZED)
    
    
    def list(self, request):
        """
        Lista todos os usuários.
        """
        queryset = Usuario.objects.all()
        serializer = UsuarioSerializer(queryset, many=True)
        return Response(serializer.data)
    