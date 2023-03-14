from dj_rest_auth.views import LogoutView
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from . import serializers


class CustomLogoutView(LogoutView):
    permission_classes = (permissions.IsAuthenticated, )


class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.RegisterSerializer


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserListSerializer
    permission_classes = (permissions.IsAuthenticated,)


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserDetailSerializer
    permission_classes = (permissions.IsAuthenticated,)
