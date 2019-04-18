from django.http import HttpResponse
from rest_framework.views import APIView

from towns.dsl import dsl_engine


class TownDsl(APIView):

    @staticmethod
    def post(request):
        result = dsl_engine.execute(**request.data)
        if isinstance(result, Exception):
            return HttpResponse(content=str(result), status=500)
        return HttpResponse(content=result)
