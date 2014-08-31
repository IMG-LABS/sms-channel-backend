from rest_framework import generics, status
from rest_framework.response import Response

from users.models import User, UserDetails
from users.serializers import UserSerializer, UserDetailsSerializer

class UserList(generics.ListCreateAPIView):
	model = User
	serializer_class = UserSerializer

class UserDetail(generics.ListCreateAPIView):
	model = UserDetails
	serializer_class = UserDetailsSerializer