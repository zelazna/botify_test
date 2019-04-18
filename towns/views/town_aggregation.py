from django.db.models import Avg, Min, Max, Count
from rest_framework.response import Response
from rest_framework.views import APIView

from towns.models import Town
from towns.serializers.aggregation_serializer import AggregationSerializer
from towns.serializers.town_serializer import TownSerializer


class TownAggregation(APIView):
    serializer_class = TownSerializer
    filter_param = 'region_code'
    agg_param = 'population'

    def get(self, request, *args, **kwargs):
        region_code = request.query_params.get(self.filter_param)
        result = Town.objects \
            .filter(department_code=region_code) \
            .aggregate(Avg(self.agg_param), Min(self.agg_param), Max(self.agg_param), count=Count('name'))
        serializer = AggregationSerializer(result)
        return Response(serializer.data)
