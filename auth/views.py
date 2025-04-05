from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer, LoginSerializer
from django.contrib.auth.models import User
from rest_framework import exceptions
from rest_framework.response import Response
from .docs import *

@extend_schema(tags=["auth"])
class AuthViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    @login_schema
    @action(detail=False, methods=["post"], url_path="login")
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            user = User.objects.get(username=request.data['username'])
            if not user.check_password(request.data['password']):
                raise exceptions.AuthenticationFailed('Password is incorrect')
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('User not found')

        user = UserSerializer(user).data
        return Response(user)

    @register_schema
    @action(detail=False, methods=["post"], url_path="register")
    def register(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user = User.objects.get(username=serializer.data['username'])
        user = UserSerializer(user).data
        return Response(user, status=201)
