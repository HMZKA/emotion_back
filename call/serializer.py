from rest_framework import serializers

from .models import Call


class CallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Call
        fields = "__all__"

    def create(self, validated_data):
        return Call.objects.create(validated_data)
