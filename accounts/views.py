from rest_framework import viewsets
from accounts.models import SubUser
from .serializers import SubUserSerializer, UserRegisterSerializer, UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from django.contrib.auth import get_user_model
from django_filters import rest_framework as filters
# Create your views here.

class RegisterUserView(CreateModelMixin, GenericViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserRegisterSerializer


class UserViewset(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class SubUserViewset(viewsets.ModelViewSet):
    queryset = SubUser.objects.all()
    serializer_class = SubUserSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('user__email','email')