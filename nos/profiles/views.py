from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from profiles.models import Profile
from profiles.serializers import ProfileSerializer
from rest_framework import viewsets


class ProfilesViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

