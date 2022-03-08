from django.shortcuts import render
from .serializers import UserSerializer, UserLoginSerializers
from rest_framework import generics,authentication,permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.views import APIView



class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class UserLoginView(ObtainAuthToken):
    serializer_class = UserLoginSerializers
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user

