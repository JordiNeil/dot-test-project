from django.shortcuts import render
from rest_framework import generics, permissions, serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CarSerializer
from .models import Car

from oauth2_provider.backends import OAuthLibCore
from oauth2_provider.contrib.rest_framework import (TokenHasReadWriteScope,
                                                    TokenHasScope)


# Create your views here.
class CarView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    serializer_class = CarSerializer
    queryset = Car.objects.all()
