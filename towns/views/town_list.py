from rest_framework import generics

from towns.models import Town
from towns.serializers.town_serializer import TownSerializer


class TownList(generics.ListAPIView):
    queryset = Town.objects.all()
    serializer_class = TownSerializer
