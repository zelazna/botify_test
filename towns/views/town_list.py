from rest_framework.response import Response
from rest_framework.views import APIView

from towns.models import Town
from towns.serializers.town_serializer import TownSerializer


class TownList(APIView):
    @staticmethod
    def get(request):
        snippets = Town.objects.all()
        serializer = TownSerializer(snippets, many=True)
        return Response(serializer.data)