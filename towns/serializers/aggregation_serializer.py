from rest_framework import serializers


class AggregationSerializer(serializers.Serializer):
    count = serializers.IntegerField(read_only=True)
    population__avg = serializers.FloatField(read_only=True)
    population__min = serializers.IntegerField(read_only=True)
    population__max = serializers.IntegerField(read_only=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
