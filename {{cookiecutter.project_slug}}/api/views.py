from django.shortcuts import render

from rest_framework import viewsets
from . import serializers, models

class ThingViewSet(viewsets.ModelViewSet):
    queryset = models.Thing.objects.all().order_by('name')
    serializer_class = serializers.ThingSerializer
