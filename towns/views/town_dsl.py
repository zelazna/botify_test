from django.http import HttpResponse
from rest_framework.views import APIView

from towns.dsl.dsl_engine import DSLEngine


class TownDsl(APIView):

    @staticmethod
    def post(request):
        result = DSLEngine().query(**request.data)
        if isinstance(result, Exception):
            return HttpResponse(content=str(result), status=500)
        return HttpResponse(content=result)
