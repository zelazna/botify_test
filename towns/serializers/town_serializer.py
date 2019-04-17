from rest_framework import serializers


class TownSerializer(serializers.Serializer):
    name = serializers.CharField(read_only=True)
    town_code = serializers.IntegerField(read_only=True)
    department_code = serializers.IntegerField(read_only=True)
    population = serializers.IntegerField(read_only=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

